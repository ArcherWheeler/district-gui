import geopandas

texas_shape_file = geopandas.read_file('../Texas_State_Boundary-shp/State.shp')
texas_shape_file.to_file('../state_plans/texas.geojson', driver = 'GeoJSON')