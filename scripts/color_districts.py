import sys
from shapely.geometry import shape, LineString, MultiLineString
import geojson

def color_district():
    with open('../pages/district_plans/phase_1/' + sys.argv[1] + '.geojson', 'r') as districts_file:
        state_districts = geojson.load(districts_file)
        districts_file.close()
        
    districts = []

    # Adds districts to list (as Shapely objects)
    for feature in state_districts["features"]:
        districts.append(shape(feature["geometry"]))

    adjacencies = [set() for i in range(len(districts))]

    # Creates adjacency list for each district
    for i in range(len(districts)):
        for j in range(i + 1, len(districts)):
            if type(districts[i].intersection(districts[j])) is LineString or type(districts[i].intersection(districts[j])) is MultiLineString:
                adjacencies[i].add(j)
                adjacencies[j].add(i)

    # degree_list[0] is the list of all districts with degree 0, degree_list[1] is the list of all districts with degree 1, and so on
    degree_list = [[]] * len(districts)

    # district_coloring_order mimics a stack where districts exist in the order in which they should be colored
    district_coloring_order = []

    # available_colors[district_coloring[i]] is the hex color district i is assigned
    district_coloring = [-1] * len(districts)

    # Initializes degree_list: For each i between 0 and number of districts - 1, generates list of districts with degree i
    for i in range(len(districts)):
        degree_list[len(adjacencies[i])].append(i)

    # Establishes order in which districts should be colored to ensure 6-coloring (i.e. district_coloring_order)
    for i in range(len(districts)):
        minimum_degree = next(index for (index, lst) in enumerate(degree_list) if lst != [])
        minimum_vertex = degree_list[minimum_degree].pop(0)
        district_coloring_order.append(minimum_vertex)

        # Update the degrees of the neighbors of minimum_vertex in degree_list
        for neighbor in adjacencies[minimum_vertex]:
            for index in range(len(degree_list)):
                if neighbor in degree_list[index]:
                    degree_list[index].remove(neighbor)
                    degree_list[index - 1].append(neighbor)
                    break

    # Assign the first district with the lowest number (i.e. color)
    district_coloring[district_coloring_order.pop(0)] = 0

    # Assign the remaining districts with a number
    while district_coloring_order:
        next_district_to_color = district_coloring_order.pop(0)
        color = 0
        adjacent_colors = set()
        for neighbor in adjacencies[next_district_to_color]:
            adjacent_colors.add(district_coloring[neighbor])

        while color in adjacent_colors:
            color += 1
        
        district_coloring[next_district_to_color] = color

    available_colors = ["#23628F", "#FF00AA", "#FFD400", "#6AFF00", "#00EAFF", "#6B238F"]

    for feature in state_districts["features"]:
        feature["properties"]["color"] = available_colors[district_coloring[districts.index(shape(feature["geometry"]))]]

    with open('../pages/district_plans/phase_1/' + sys.argv[1] + '.geojson', 'w') as districts_file:
        geojson.dump(state_districts, districts_file)

color_district()