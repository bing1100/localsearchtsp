import generatedata
import random
import math
from route import Route

def linear_schedule(T, init, step):
    return T - 0.0001 * T

def exp_schedule(T, init, step):
    return 0.96 * T

def boltzman_schedule(T, init, step):
    return init / math.log(step)

def sim_annealing(points, anneal_schedule, init_temp = 10000, data = None):
    T = init_temp

    r = Route(points, data)
    step = 2

    while T > 0.00001:
        list_2opt = r.list_2opt()

        idx = random.randint(0, len(list_2opt) - 1)
        delta = list_2opt[idx]

        if delta > 0:
            r.swap_at(idx)
        else:
            p = math.exp(delta/T) * 100
            if random.randint(0, 100) <= p:
                r.swap_at(idx)
        
        T = anneal_schedule(T, init_temp, step)
        step += 1
    
    return [r.distance(), r.data, step]

if __name__ == "__main__":
    points = generatedata.parsefile(14,5)

    shared_data = [point[0] for point in points[1:]]
    random.shuffle(shared_data)

    print(sim_annealing(points, linear_schedule, data=shared_data))
    print(sim_annealing(points, exp_schedule, data=shared_data, init_temp=1000000))
    print(sim_annealing(points, boltzman_schedule, data=shared_data, init_temp=0.0001))



