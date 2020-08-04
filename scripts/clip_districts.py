import geojson
from shapely.geometry import shape

with open('state_plans/texas_state.geojson', 'r') as texas_state_file:
    texas_state = geojson.load(texas_state_file)

with open('district_plans/texas.geojson', 'r') as texas_districts_file:
    texas_districts = geojson.load(texas_districts_file)

clipped_districts = []

texas_polygon = shape(texas_state["features"][0]["geometry"])
for feature in texas_districts["features"]:
    district_polygon = shape(feature["geometry"])
    clipped_districts.append(texas_polygon.intersection(district_polygon))

feature_collection = geojson.FeatureCollection(clipped_districts)

with open('district_plans/texas_clipped.geojson', 'w') as texas_clipped_file:
    geojson.dump(feature_collection, texas_clipped_file)