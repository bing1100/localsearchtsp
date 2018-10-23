import generatedata
import random
import copy
from route import Route
from tabu import TabuList

def best_sol(list_sol):
    return min(range(len(list_sol)), key=list_sol.__getitem__)

def hc(points, data = None):
    r = Route(points, data)
    steps = 0

    improvement = True
    while improvement:
        improvement = False
        for i in range(len(points) - 1):
            for k in range(i + 1, len(points) - 1):
                new_route = r.swap_at(i, k)
                new_distance = r.distance(new_route)

                if new_distance < r.dist:
                    r.set_route(new_route, new_distance)
                    steps += 1
                    improvement = True
                    break

            if improvement:
                break
    
    return [r.dist, r.data, steps]

def hc_tabu(points, data = None):
    r = Route(points, data)
    tabu = TabuList(100)
    sideways = 100
    steps = 0

    improvement = True
    while improvement:
        improvement = False
        for i in range(len(points) - 1):
            for k in range(i + 1, len(points) - 1):
                new_route = r.swap_at(i, k)
                new_distance = r.distance(new_route)

                if new_distance < r.dist:
                    r.set_route(new_route, new_distance)
                    steps += 1
                    improvement = True
                    sideways = 100
                    break
                elif new_distance < (r.dist + 0.001):
                    if (sideways != 0 and tabu.check_and_add(new_route)):
                        r.set_route(new_route, new_distance)
                        steps += 1
                        improvement = True
                        sideways -= 1

            if improvement:
                break
    
    return [r.dist, r.data, steps]

def hc_random_restart(points, max_restarts):
    list_sol = []
    num = 0

    while num < max_restarts:
        list_sol.append(hc(points))
        num += 1

    min_idx = best_sol(list_sol)

    return list_sol[min_idx]
    
if __name__ == "__main__":
    points = generatedata.parsefile(14,5)

    shared_data = [point[0] for point in points[1:]]
    random.shuffle(shared_data)

    shared_data2 = copy.deepcopy(shared_data)

    print(hc(points, shared_data))
    print(hc_tabu(points, shared_data2))

    print(hc_random_restart(points, 100))



    



