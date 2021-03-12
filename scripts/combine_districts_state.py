import geojson
import sys

with open('../pages/district_plans/phase_1/' + sys.argv[1] + '.geojson', 'r') as phase_one_file:
        phase_one_districts = geojson.load(phase_one_file)
        phase_one_file.close()
        
# with open('../pages/district_plans/phase_2/' + sys.argv[1] + '.geojson', 'r') as phase_two_file:
#         phase_two_districts = geojson.load(phase_two_file)
#         phase_two_file.close()

with open('../state_plans/' + sys.argv[1] + '.geojson', 'r') as state_file:
    state = geojson.load(state_file)

state_dict = {
    "type": "Feature",
    "properties": {
    "color": "None"
    }
}

state_dict["geometry"] = state
phase_one_districts["features"].append(state_dict)
# phase_two_districts["features"].append(state_dict)

with open('../pages/district_plans/phase_1/' + sys.argv[1] + '.geojson', 'w') as phase_one_file:
    geojson.dump(phase_one_districts, phase_one_file)
    
# with open('../pages/district_plans/phase_2/' + sys.argv[1] + '.geojson', 'w') as phase_two_file:
#     geojson.dump(phase_two_districts, phase_two_file)

