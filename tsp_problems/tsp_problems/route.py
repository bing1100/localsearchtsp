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

    def distance(self):
        total_dist = 0

        first_path = 'A' + str(self.data[0])
        total_dist += self.dict_dist[first_path]

        from_city = str(self.data[0])
        for to_city in self.data[1:]:
            name = edge_name(from_city, to_city)
            total_dist += self.dict_dist[name]
            from_city = to_city
        
        last_path = 'A' + from_city
        total_dist += self.dict_dist[last_path]

        return total_dist

    def list_2opt(self):
        list_2opt = []

        prev_city = 'A'
        from_city = str(self.data[0])
        to_city = str(self.data[1])
        next_city = str(self.data[2])

        o_dist = self.dict_dist[prev_city + from_city]
        o_dist += self.dict_dist[edge_name(to_city, next_city)]
        n_dist = self.dict_dist[prev_city + to_city]
        n_dist += self.dict_dist[edge_name(from_city, next_city)]
        list_2opt.append(o_dist - n_dist)

        prev_city = from_city
        for idx in range(1, len(self.data) - 2):
            from_city = self.data[idx]
            to_city = self.data[idx + 1]
            next_city = self.data[idx + 2]
            
            o_dist = self.dict_dist[edge_name(prev_city, from_city)]
            o_dist += self.dict_dist[edge_name(to_city, next_city)]
            n_dist = self.dict_dist[edge_name(prev_city, to_city)]
            n_dist += self.dict_dist[edge_name(from_city, next_city)]
            list_2opt.append(o_dist - n_dist)

            prev_city = from_city

        from_city = str(self.data[-2])
        to_city = str(self.data[-1])
        next_city = 'A'

        o_dist = self.dict_dist[edge_name(prev_city, from_city)]
        o_dist += self.dict_dist[next_city + to_city]
        n_dist = self.dict_dist[edge_name(prev_city, to_city)]
        n_dist += self.dict_dist[next_city + from_city]
        list_2opt.append(o_dist - n_dist)

        return list_2opt

    def swap_at(self, idx):
        temp = self.data[idx]
        self.data[idx] = self.data[idx + 1]
        self.data[idx + 1] = temp 
        
if __name__ ==  "__main__":

    points = generatedata.parsefile(14,5)
    route = Route(points)
    print(route.data)

    old_d = route.distance()
    list_2opt = route.list_2opt()
    
    for idx in range(len(list_2opt)):

        route.swap_at(idx)
        print(route.data)
        new_d = route.distance()
        if abs(old_d - new_d) > abs(list_2opt[idx]) + 0.00001:
            print(abs(old_d - new_d), abs(list_2opt[idx]) + 0.00001)
            print("Error")
        route.swap_at(idx)
        





