import hc
import annealing
import generatedata
from time import time

points = generatedata.parsefile_p36()

print("=====")
print("Test the 36 city Problem: ")
print("=====")

print("Hill Climbing: ")
start = time()
a_quality, sol, steps = hc.hc(points)
print("Sol cost: ", a_quality)
print("Sol route: ", sol)
print("Num Steps: ", steps)
print("Time Elapsed: ",time() - start)

print("=====")
print("Hill Climbing (10 restarts): ")
start = time()
a_quality, sol, steps = hc.hc_random_restart(points, 10)
print("Sol cost: ", a_quality)
print("Sol route: ", sol)
print("Num Steps: ", steps)
print("Time Elapsed: ",time() - start)

print("=====")
print("Linear Annealing: ")
start = time()
a_quality, sol, steps = annealing.sim_annealing(points, annealing.linear_schedule, init_temp=900000000)
print("Sol cost: ", a_quality)
print("Sol route: ", sol)
print("Num Steps: ", steps)
print("Time Elapsed: ",time() - start)

print("=====")
print("EXP Annealing: ")
start = time()
a_quality, sol, steps = annealing.sim_annealing(points, annealing.exp_schedule, init_temp=900000000)
print("Sol cost: ", a_quality)
print("Sol route: ", sol)
print("Num Steps: ", steps)
print("Time Elapsed: ",time() - start)

print("=====")
print("Boltzman Annealing: ")
start = time()
a_quality, sol, steps = annealing.sim_annealing(points, annealing.boltzman_schedule, init_temp=0.0001)
print("Sol cost: ", a_quality)
print("Sol route: ", sol)
print("Num Steps: ", steps)
print("Time Elapsed: ",time() - start)
