import generatedata
import random

# Calculate the edge name for two points
def gen_name(point_a, point_b):
    edge_name = [point_a[0], point_b[0]]
    if (point_a[0] > point_b[0]):
        edge_name = [point_b[0], point_a[0]]
    return edge_name

# Calculate the euclidean distance
def calc_dist(point_a, point_b):
    edge_name = gen_name(point_a, point_b)
    dist = ((point_a[1][0] - point_b[1][0])**2 + (point_a[1][1] - point_b[1][1])**2)**(1/2)
    return [dist, edge_name]

# Calculate the name of the edge
def edge_name(point_a, point_b):
    edge_name = gen_name(point_a, point_b)
    return ''.join(edge_name)

# Create the sorted list of edges.
def create_dict_dist(points):
    dict_edges = {}
    for i in range(len(points)):
        point_a = points[i]
        for j in range(i + 1, len(points)):
            point_b = points[j]
            dist = calc_dist(point_a, point_b)

            dict_edges[''.join(dist[1])] = dist[0]
    return dict_edges

# A Route class that stores all the data for the Route
class Route():

    # Initialize the route either with predefined initial route or a set of points
    def __init__(self, points, data = None):
        # Create a dictionary of edge costs from the points
        self.dict_dist = create_dict_dist(points)

        # Set the initial route data 
        if data != None:
            self.data = data # predefined initial route
        else:
            self.data = [point[0] for point in points[1:]]
            random.shuffle(self.data) # randomized initial route

        # Set the initial distance
        self.dist = self.distance(self.data)

    # Calculate the total distance for the route 
    def distance(self, data):
        total_dist = 0

        first_path = edge_name(["A"], data)
        total_dist += self.dict_dist[first_path]

        from_city = str(data[0])
        for to_city in data[1:]:
            name = edge_name(from_city, to_city)
            total_dist += self.dict_dist[name]
            from_city = to_city
        
        last_path = edge_name(["A"], from_city)
        total_dist += self.dict_dist[last_path]

        return total_dist

    # Get the distance for the current route
    def get_distance(self):
        return self.dist

    # Create a new route with a 2opt swap from i to k
    def swap_at(self, i, k):
        new_route = self.data[0:i]
        new_route.extend(reversed(self.data[i:k+1]))
        new_route.extend(self.data[k+1:])

        return new_route

    # Set the new route data and distance
    def set_route(self, new_route, distance):
        self.data = new_route
        self.dist = distance

# Unit tests
if __name__ ==  "__main__":

    points = generatedata.parsefile(14,5)
    route = Route(points)
    print(route.data)

    old_d = route.distance(route.data)
    
        





