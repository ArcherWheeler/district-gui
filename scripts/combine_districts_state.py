import geojson
import sys

with open('../district_plans/' + sys.argv[1] + '.geojson', 'r') as districts_file:
        state_districts = geojson.load(districts_file)
        districts_file.close()

with open('../state_plans/' + sys.argv[1] + '.geojson', 'r') as state_file:
    state = geojson.load(state_file)

state_dict = {
    "type": "Feature",
    "properties": {
    "color": "None"
    }
}

state_dict["geometry"] = state
state_districts["features"].append(state_dict)

with open('../district_plans/' + sys.argv[1] + '.geojson', 'w') as districts_file:
    geojson.dump(state_districts, districts_file)

