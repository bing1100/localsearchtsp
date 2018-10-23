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


class Route():
    def __init__(self, points, data = None):
        self.dict_dist = create_dict_dist(points)
        if data != None:
            self.data = data
        else:
            self.data = [point[0] for point in points[1:]]
            random.shuffle(self.data)
        self.dist = self.distance(self.data)

    def distance(self, data):
        total_dist = 0

        first_path = 'A' + str(data[0])
        total_dist += self.dict_dist[first_path]

        from_city = str(data[0])
        for to_city in data[1:]:
            name = edge_name(from_city, to_city)
            total_dist += self.dict_dist[name]
            from_city = to_city
        
        last_path = 'A' + from_city
        total_dist += self.dict_dist[last_path]

        return total_dist

    def get_distance(self):
        return self.dist

    def swap_at(self, i, k):
        new_route = self.data[0:i]
        new_route.extend(reversed(self.data[i:k+1]))
        new_route.extend(self.data[k+1:])

        return new_route

    def set_route(self, new_route, distance):
        self.data = new_route
        self.dist = distance

        
if __name__ ==  "__main__":

    points = generatedata.parsefile(14,5)
    route = Route(points)
    print(route.data)

    old_d = route.distance(route.data)
    
        





