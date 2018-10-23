import annealing
import matplotlib
import generatedata
import random
import copy
from progressbar import progress

print("Printing linear Averages")
opt_sol = generatedata.parsefile_opt()

avg = []
count = 0
for num_city in range(14, 17):
    city_sum = [0, 0, 0]

    for instance in range(1, 3):
        instance_sum = [0, 0, 0]
        points = generatedata.parsefile(num_city, instance)

        for it in range(100):
            a_quality, sol, steps = annealing.sim_annealing(points, annealing.linear_schedule, init_temp=10000)
            idx = (num_city - 14) * 10 + instance - 1
            instance_sum[0] += a_quality / opt_sol[idx]
            instance_sum[1] += steps

            if abs(a_quality - opt_sol[idx]) < 0.1:
                instance_sum[2] += 1 

            count += 1
            progress(count, 600)

        city_sum = [ city_sum[i] + instance_sum[i]/100 for i in range(3) ]

    city_avg = [ val/2 for val in city_sum ]
    avg.append(city_avg)

print(avg)

print("Printing exp Averages")
opt_sol = generatedata.parsefile_opt()

avg = []
count = 0
for num_city in range(14, 17):
    city_sum = [0, 0, 0]

    for instance in range(1, 3):
        instance_sum = [0, 0, 0]
        points = generatedata.parsefile(num_city, instance)

        for it in range(100):
            a_quality, sol, steps = annealing.sim_annealing(points, annealing.exp_schedule, init_temp=900000000)
            idx = (num_city - 14) * 10 + instance - 1
            instance_sum[0] += a_quality / opt_sol[idx]
            instance_sum[1] += steps

            if abs(a_quality - opt_sol[idx]) < 0.1:
                instance_sum[2] += 1 

            count += 1
            progress(count, 600)

        city_sum = [ city_sum[i] + instance_sum[i]/100 for i in range(3) ]

    city_avg = [ val/2 for val in city_sum ]
    avg.append(city_avg)

print(avg)

print("Printing Boltzman Averages")
opt_sol = generatedata.parsefile_opt()

avg = []
count = 0
for num_city in range(14, 17):
    city_sum = [0, 0, 0]

    for instance in range(1, 3):
        instance_sum = [0, 0, 0]
        points = generatedata.parsefile(num_city, instance)

        for it in range(100):
            a_quality, sol, steps = annealing.sim_annealing(points, annealing.boltzman_schedule, init_temp=0.0001)
            idx = (num_city - 14) * 10 + instance - 1
            instance_sum[0] += a_quality / opt_sol[idx]
            instance_sum[1] += steps

            if abs(a_quality - opt_sol[idx]) < 0.1:
                instance_sum[2] += 1
            
            count += 1
            progress(count, 600)

        city_sum = [ city_sum[i] + instance_sum[i]/100 for i in range(3) ]

    city_avg = [ val/2 for val in city_sum ]
    avg.append(city_avg)

print(avg)