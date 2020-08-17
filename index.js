import 'ol/ol.css';
import Map from 'ol/Map';
import View from 'ol/View';
import GeoJSON from 'ol/format/GeoJSON';
import {Tile as TileLayer, Vector as VectorLayer} from 'ol/layer';
import {OSM, Vector as VectorSource} from 'ol/source';
import {Circle as CircleStyle, Fill, Stroke, Style} from 'ol/style';
import 'fs';

const districtPlans = require('./district_plans/*.geojson');
const statePlans = require('./state_plans/*.geojson');

// Hacky global vars to update / delete layers from the open layer map app
var currentDistrictLayer = null;
var currentStateLayer = null;

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

const urlHashPart = () => window.location.hash.substr(1)

const updateMap = (mapToDisplay) => {
  if (currentDistrictLayer != null) {
    map.removeLayer(currentDistrictLayer);
    map.removeLayer(currentStateLayer);
  }

  if (mapToDisplay in districtPlans) {
    fetch(districtPlans[mapToDisplay])
    .then(response => response.json())
    .then(data => {
      const districtVectorLayer = new VectorLayer({
        source: new VectorSource({
          features: (new GeoJSON()).readFeatures(data)
        }),
        style: function (feature) {
          return new Style({
            fill: new Fill({
              color: hexToRGB(feature.get('color'), 0.3)
            })
          })
        }
      });
      currentDistrictLayer = districtVectorLayer;
      map.addLayer(districtVectorLayer);
    })

    fetch(statePlans[mapToDisplay])
    .then(response => response.json())
    .then(data => {
      const stateVectorLayer = new VectorLayer({
        source: new VectorSource({
          features: (new GeoJSON()).readFeatures(data)
        }),
        style: new Style({
          stroke: new Stroke({
            color: 'black',
            width: 2
          })
        })
      });
      currentStateLayer = stateVectorLayer;
      map.addLayer(stateVectorLayer);
    })
  }
}

updateMap(urlHashPart());

window.onhashchange = function() {
  updateMap(urlHashPart());
}
