import geojson
import sys
from shapely.geometry import shape, LineString, MultiLineString

with open('../district_plans/texas.geojson', 'r') as texas_districts_file:
    texas_districts = geojson.load(texas_districts_file)
    texas_districts_file.close()

districts = list()

# Adds districts to list (as Shapely objects)
for feature in texas_districts["features"]:
    districts.append(shape(feature["geometry"]))

adjacencies = [set() for i in range(len(districts))]

# Creates adjacency list for each district
for i in range(len(districts)):
    for j in range(i + 1, len(districts)):
        if type(districts[i].intersection(districts[j])) is LineString or type(districts[i].intersection(districts[j])) is MultiLineString:
            adjacencies[i].add(j)
            adjacencies[j].add(i)

degree_list = [list()] * len(districts)
coloring_order = list()
coloring = [-1] * len(districts)

# Creates list of districts with degree i (for i between 0 and number of districts - 1)
for i in range(len(districts)):
    degree_list[len(adjacencies[i])].append(i)

# Establishes order in which districts should be colored to ensure 6-coloring
for i in range(len(districts)):
    minimum_degree = next(index for (index, lst) in enumerate(degree_list) if lst)
    minimum_vertex = degree_list[minimum_degree].pop(0)
    coloring_order.append(minimum_vertex)

    for neighbor in adjacencies[minimum_vertex]:
        for index in range(len(degree_list)):
            if neighbor in degree_list[index]:
                degree_list[index].remove(neighbor)
                degree_list[index - 1].append(neighbor)
                break

# Assign the first district with the lowest number.
coloring[coloring_order.pop(0)] = 0

# Assign the remaining districts with a number.
while coloring_order:
    vertex = coloring_order.pop(0)
    color = 0
    adjacent_colors = set()
    for adjacent in adjacencies[vertex]:
        adjacent_colors.add(coloring[adjacent])

    while color in adjacent_colors:
        color += 1
    
    coloring[vertex] = color

available_colors = ["#23628F", "#FF00AA", "#FFD400", "#6AFF00", "#00EAFF", "#6B238F"]

for feature in texas_districts["features"]:
    feature["properties"]["color"] = available_colors[coloring[districts.index(shape(feature["geometry"]))]]

with open('../district_plans/texas.geojson', 'w') as texas_districts_file:
    geojson.dump(texas_districts, texas_districts_file)