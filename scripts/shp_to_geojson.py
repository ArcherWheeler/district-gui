import geopandas

shape_file = geopandas.read_file('../Congressional_Districts-shp/2a3f5ece-e912-4099-9a63-56417f74a25e202044-1-zjh6dc.92ezj.shp')
shape_file.to_file('../current_district_plans/RI.geojson', driver = 'GeoJSON')