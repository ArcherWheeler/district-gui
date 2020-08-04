import 'ol/ol.css';
import Map from 'ol/Map';
import View from 'ol/View';
import GeoJSON from 'ol/format/GeoJSON';
import {Tile as TileLayer, Vector as VectorLayer} from 'ol/layer';
import {OSM, Vector as VectorSource} from 'ol/source';
import {Circle as CircleStyle, Fill, Stroke, Style} from 'ol/style';
import 'fs';

const districtPlans = require('./district_plans/*.geojson');

// Hacky global var to update / delete layers from the open layer map app
var currentLayer = null;

var styles = {};

const styleFunction = (feature) => {
  return styles[feature.getGeometry().getType()];
};

var map = new Map({
  layers: [
    new TileLayer({
      source: new OSM()
    })
  ],
  target: 'map',
  view: new View({
    projection: 'EPSG:4326',
    center: [-97.260204, 38.582526],
    zoom: 4.5
  })
});

const urlHashPart = () => window.location.hash.substr(1)

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
        })
      });

      vectorLayer.getSource().forEachFeature(function(feature) {
        styles = {
          'Polygon': new Style({
            stroke: new Stroke({
              color: 'black',
              lineDash: [4],
              width: 3
            }),
            fill: new Fill({
              color: 'rgba(' + Math.floor(Math.random() * 256) + ", " + Math.floor(Math.random() * 256)
              + ', ' + Math.floor(Math.random() * 256) + ', 0.3)'       
            })
          })
        };
        feature.setStyle(styleFunction(feature));
      });
      currentLayer = vectorLayer;
      map.addLayer(vectorLayer);
    })
  }
}

updateMap(urlHashPart());

window.onhashchange = function() {
  updateMap(urlHashPart());
}
