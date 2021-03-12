import geopandas
import geojson

# shape_file = geopandas.read_file('/Users/beenish/Documents/district-gui/gz_2010_us_040_00_500k/gz_2010_us_040_00_500k.shp')
# shape_file.to_file('../state_plans/states.geojson', driver = 'GeoJSON')

with open('../state_plans/states.geojson', 'r') as states_file:
    states = geojson.load(states_file)["features"]
    
for state in states:
    if state["properties"]["NAME"] == "New Jersey":
        with open('../state_plans/NJ.geojson', 'w') as NJ_state_file:
            geojson.dump(state["geometry"], NJ_state_file)
            
        # with open('../pages/district_plans/phase_1/OH.geojson', 'w') as OH_phase_one_file:
        #     phase_one_dict = {
        #         "type": "FeatureCollection",
        #         "features": [
        #             {
        #                 "type": "Feature",
        #                 "properties": {
        #                     "color": "#23628F"
        #                 },
        #                 "geometry": state["geometry"]
        #             }
        #         ],
        #     }
        #     geojson.dump(phase_one_dict, OH_phase_one_file)
            
        # with open('../pages/district_plans/phase_2/OH.geojson', 'w') as OH_phase_two_file:
        #     phase_two_dict = {
        #         "type": "FeatureCollection",
        #         "features": [
        #             {
        #                 "type": "Feature",
        #                 "properties": {
        #                     "color": "#23628F"
        #                 },
        #                 "geometry": state["geometry"]
        #             }
        #         ],
        #     }
        #     geojson.dump(phase_two_dict, OH_phase_two_file)