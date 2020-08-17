import geojson
from shapely.geometry import shape, mapping

with open('../state_plans/texas.geojson', 'r') as texas_state_file:
    texas_state = geojson.load(texas_state_file)

with open('../district_plans/texas.geojson', 'r') as texas_districts_file:
    texas_districts = geojson.load(texas_districts_file)
    texas_districts_file.close()

texas_polygon = shape(texas_state["features"][0]["geometry"])
for feature in texas_districts["features"]:
    district_polygon = shape(feature["geometry"])
    feature["geometry"] = mapping(texas_polygon.intersection(district_polygon))

with open('../district_plans/texas.geojson', 'w') as texas_districts_file:
    geojson.dump(texas_districts, texas_districts_file)