import geojson
import sys
from shapely.geometry import shape, LineString, MultiLineString

with open('../district_plans/texas.geojson', 'r') as texas_districts_file:
    texas_districts = geojson.load(texas_districts_file)
    texas_districts_file.close()

districts = []

for feature in texas_districts["features"]:
    districts.append(shape(feature["geometry"]))

adjacencies = [set() for i in range(len(districts))]

for i in range(len(districts)):
    for j in range(i + 1, len(districts)):
        if type(districts[i].intersection(districts[j])) is LineString or type(districts[i].intersection(districts[j])) is MultiLineString:
            adjacencies[i].add(j)
            adjacencies[j].add(i)

coloring = [-1 for i in range(len(districts))]

# Assign the first vertex with the lowest number.
coloring[0] = 0

for vertex in range(1, len(coloring)):
    color = 0
    adjacent_colors = set()
    for adjacent in adjacencies[vertex]:
        adjacent_colors.add(coloring[adjacent])

    while color in adjacent_colors:
        color += 1

    coloring[vertex] = color

available_colors = ["#FF0000", "#FFFF00", "#00EAFF", "#AA00FF", "#4F8F23", "#BFFF00", 
"#0095FF", "#FF00AA", "#FFD400", "#6AFF00", "#0040FF", "#EDB9B9", "#B9D7ED", "#E7E9B9", 
"#DCB9ED", "#B9EDE0", "#8F2323", "#23628F", "#8F6A23", "#6B238F", "#FF7F00"]

for feature in texas_districts["features"]:
    feature["properties"]["color"] = available_colors[coloring[districts.index(shape(feature["geometry"]))]]

with open('../district_plans/texas.geojson', 'w') as texas_districts_file:
    geojson.dump(texas_districts, texas_districts_file)
