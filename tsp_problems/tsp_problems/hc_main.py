import hc
import matplotlib
import generatedata
import random
import copy

print("Printing Averages")
opt_sol = generatedata.parsefile_opt()

idx = 0
avg = [] 
for num_city in range(14, 17):
    city_sum = [0, 0, 0]

    for instance in range(1, 11):
        instance_sum = [0, 0, 0]
        points = generatedata.parsefile(num_city, instance)

        for it in range(100):
            a_quality, sol, steps = hc.hc(points)

            instance_sum[0] += a_quality
            instance_sum[1] += steps

            if abs(a_quality - opt_sol[idx]) < 0.1:
                instance_sum[2] += 1 


        idx += 1
        city_sum = [ city_sum[i] + instance_sum[i]/100 for i in range(3) ]

    city_avg = [ val/10 for val in city_sum ]
    avg.append(city_avg)

print(avg)

print("Tabu does not help TSP")

for num_city in range(14, 17):
    for instance in range(1, 11):
        points = generatedata.parsefile(num_city, instance)
        shared_data = [point[0] for point in points[1:]]
        random.shuffle(shared_data)
        shared_data2 = copy.deepcopy(shared_data)

        sol = hc.hc(points, shared_data)
        sol2 = hc.hc_tabu(points, shared_data2)

        if sol != sol2:
            print("False", num_city, instance)
