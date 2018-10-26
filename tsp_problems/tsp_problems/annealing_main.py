import annealing
import matplotlib
import generatedata
import random
import copy
from progressbar import progress
from time import time

opt_sol = generatedata.parsefile_opt()

print("=====")
print("Printing linear Averages")
print("=====")

start = time()
avg = []
count = 0
for num_city in range(14, 17):
    city_sum = [0, 0, 0]

    for instance in range(1, 3):
        instance_sum = [0, 0, 0]
        points = generatedata.parsefile(num_city, instance)

        for it in range(100):
            a_quality, sol, steps = annealing.sim_annealing(points, annealing.linear_schedule, init_temp=900000000)
            idx = (num_city - 14) * 10 + instance - 1
            instance_sum[0] += a_quality / opt_sol[idx]
            instance_sum[1] += steps

            if abs(a_quality - opt_sol[idx]) < 0.1:
                instance_sum[2] += 1 

            count += 1
            progress(count, 600, "Linear Annealing")

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

print("=====")
print("Printing exp Averages")
print("=====")

start = time()
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
            progress(count, 600, "EXP Annealing")

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

print("=====")
print("Printing Boltzman Averages")
print("=====")

start = time()
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
            progress(count, 600, "Boltzman Annealing")

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