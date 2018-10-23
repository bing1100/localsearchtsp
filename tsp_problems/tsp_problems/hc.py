import generatedata
import random
import copy
from route import Route
from tabu import TabuList

def max_2opt(list_2opt):
    return max(range(len(list_2opt)), key=list_2opt.__getitem__)

def best_sol(list_sol):
    return min(range(len(list_sol)), key=list_sol.__getitem__)

def hc(points, data = None):
    r = Route(points, data)
    steps = 0

    while True:
        list_2opt = r.list_2opt()

        max_idx = max_2opt(list_2opt)
        max_value = list_2opt[max_idx]
        if max_value <= 0:
            break
        else:
            r.swap_at(max_idx)
            steps += 1
    
    return [r.distance(), r.data, steps]

def hc_tabu(points, data = None):
    r = Route(points, data)
    tabu = TabuList(100)
    sideways = 100
    steps = 0

    while True:
        list_2opt = r.list_2opt()

        max_idx = max_2opt(list_2opt)
        max_value = list_2opt[max_idx]

        if max_value < -0.00001 :
            break
        elif abs(max_value) < 0.00001:
            r.swap_at(max_idx)
            
            if (sideways == 0 or tabu.check_and_add(r.data)):
                r.swap_at(max_idx)
                break
            
            steps += 1
            sideways -= 1
        else:
            r.swap_at(max_idx)
            steps += 1
            sideways = 100
    
    return [r.distance(), r.data, steps]

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



    



