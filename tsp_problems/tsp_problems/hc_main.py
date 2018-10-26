import hc
import matplotlib
import generatedata
import random
import copy
from progressbar import progress
from time import time

opt_sol = generatedata.parsefile_opt()

print("=====")
print("Results for hill climbing without restarts: ")
print("=====")

idx = 0
count = 0
avg = [] 
for num_city in range(14, 17):
    city_sum = [0, 0, 0]

    for instance in range(1, 11):
        instance_sum = [0, 0, 0]
        points = generatedata.parsefile(num_city, instance)

        for it in range(100):
            a_quality, sol, steps = hc.hc(points)

            instance_sum[0] += a_quality / opt_sol[idx]
            instance_sum[1] += steps

            if abs(a_quality - opt_sol[idx]) < 0.1:
                instance_sum[2] += 1 

            progress(count, 3000, "HC without restarts")
            count += 1
            
        idx += 1
        city_sum = [ city_sum[i] + instance_sum[i]/100 for i in range(3) ]

        print("Number of cities: ", num_city)
        print("Instance: ", instance)
        print("Average solution quality (%% of best): ", instance_sum[0])
        print("Average steps: ", instance_sum[1]/100)
        print("Percentage of solutions optimal: ", instance_sum[2])
        print("=====")
        # print(instance_sum[0],",", instance_sum[1]/100,",", instance_sum[2]) # For excel

    city_avg = [ val/10 for val in city_sum ]
    avg.append(city_avg)
    print("//== Overall ==//")
    print("Number of cities: ", num_city)
    print("Average solution quality (%% of best): ", city_avg[0] * 100)
    print("Average steps: ", city_avg[1])
    print("Percentage of solutions optimal: ", city_avg[2] * 100)
    print("=====")

print("Raw data format: ")
print(avg)

print("=====")
print("Results for Sidways moves and Tabu list: ")
print("=====")
for num_city in range(14, 17):
    print("Number of city: ", num_city)
    for instance in range(1, 11):
        points = generatedata.parsefile(num_city, instance)
        shared_data = [point[0] for point in points[1:]]
        random.shuffle(shared_data)
        shared_data2 = copy.deepcopy(shared_data)

        sol = hc.hc(points, shared_data)
        sol2 = hc.hc_tabu(points, shared_data2)

        print("Are answer the same for instance ", instance,": ", sol[0] == sol2[0])

print("=====")
print("Results for hill climbing with restart: ")
print("=====")

start = time()
max_restarts = [2,2,3]
avg = [] 
count = 0
for num_city in range(14, 17):
    city_sum = [0, 0, 0]

    for instance in range(1, 3):
        instance_sum = [0, 0, 0]
        points = generatedata.parsefile(num_city, instance)

        for it in range(100):
            a_quality, sol, steps = hc.hc_random_restart(points, max_restarts[num_city - 14])
            idx = (num_city - 14) * 10 + instance - 1
            instance_sum[0] += a_quality / opt_sol[idx]
            instance_sum[1] += steps

            if abs(a_quality - opt_sol[idx]) < 0.1:
                instance_sum[2] += 1 
            
            progress(count, 600, "HC with restarts")
            count += 1

        city_sum = [ city_sum[i] + instance_sum[i]/100 for i in range(3) ]
        print("Number of cities: ", num_city)
        print("Instance: ", instance)
        print("Average solution quality (%% of best): ", instance_sum[0])
        print("Average steps: ", instance_sum[1]/100)
        print("Percentage of solutions optimal: ", instance_sum[2])
        print("=====")

        # print(instance_sum[0],",", instance_sum[1]/100,",", instance_sum[2]) # For Excel
        # print(instance_sum[0],",", time() - start) # For Excel
        # start = time()

    city_avg = [ val/2 for val in city_sum ]
    avg.append(city_avg)
    print("//== Overall ==//")
    print("Number of cities: ", num_city)
    print("Average solution quality (%% of best): ", city_avg[0] * 100)
    print("Average steps: ", city_avg[1])
    print("Percentage of solutions optimal: ", city_avg[2] * 100)
    print("=====")

print("Raw data format: ")
print(avg)