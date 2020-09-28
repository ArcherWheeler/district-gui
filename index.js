import 'ol/ol.css';
import Feature from 'ol/Feature';
import Polygon from 'ol/geom/Polygon';
import Map from 'ol/Map';
import View from 'ol/View';
import GeoJSON from 'ol/format/GeoJSON';
import {Tile as TileLayer, Vector as VectorLayer} from 'ol/layer';
import {OSM, Vector as VectorSource} from 'ol/source';
import {Circle as CircleStyle, Fill, Stroke, Style} from 'ol/style';
import * as olExtent from 'ol/extent';
import 'fs';

const districtPlans = require('./district_plans/*.geojson');

// Hacky global var to update / delete layers from the open layer map app
var currentLayer = null;

var view = new View({
  projection: 'EPSG:4326',
  center: [-97.260204, 38.582526],
  zoom: 4.5
});

var map = new Map({
  layers: [
    new TileLayer({
      source: new OSM()
    })
  ],
  target: 'map',
  view: view
});

function hexToRGB(hex, alpha) {
  var r = parseInt(hex.slice(1, 3), 16),
      g = parseInt(hex.slice(3, 5), 16),
      b = parseInt(hex.slice(5, 7), 16);

  if (alpha) {
      return "rgba(" + r + ", " + g + ", " + b + ", " + alpha + ")";
  } else {
      return "rgb(" + r + ", " + g + ", " + b + ")";
  }
}

const urlHashPart = () => document.getElementById('map-dropdown').value;

const updateMap = (mapToDisplay) => {
  if (currentLayer != null) {
    map.removeLayer(currentLayer);
  }

  if (mapToDisplay in districtPlans) {
    fetch(districtPlans[mapToDisplay])
    .then(response => response.json())
    .then(data => {
      const vectorLayer = new VectorLayer({
        source: new VectorSource({
          features: (new GeoJSON()).readFeatures(data)
        }),
        style: function (feature) {
          if (feature.get('color') === 'None') {
            return new Style({
              stroke: new Stroke({
                color: 'black',
                width: 2
              })
            })
          } else {
            return new Style({
              fill: new Fill({
                color: hexToRGB(feature.get('color'), 0.3)
              })
            })
          }
        }
      });
      vectorLayer.getSource().forEachFeature(function(feature) {
        if(feature.get('color') === 'None') {
          var polygon = feature.getGeometry();
          view.fit(polygon, {padding: [50, 50, 50, 50]});
        }
      });
      currentLayer = vectorLayer;
      map.addLayer(vectorLayer);
    })
  }
}

updateMap(urlHashPart());

window.onchange = function() {
  updateMap(urlHashPart());
}
