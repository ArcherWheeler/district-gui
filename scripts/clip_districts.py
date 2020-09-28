import sys
import geojson
from shapely.geometry import shape, mapping

with open('../state_plans/' + sys.argv[1] + '.geojson', 'r') as state_file:
    state = geojson.load(state_file)
    
with open('../district_plans/' + sys.argv[1] + '.geojson', 'r') as districts_file:
    districts = geojson.load(districts_file)
    districts_file.close()
    
state_polygon = shape(state)

for feature in districts["features"]:
    district_polygon = shape(feature["geometry"])
    feature["geometry"] = mapping(state_polygon.intersection(district_polygon))
    
with open('../district_plans/' + sys.argv[1] + '.geojson', 'w') as districts_file:
    geojson.dump(districts, districts_file)