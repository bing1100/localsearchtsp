import generatedata
import random
import copy
from route import Route
from tabu import TabuList

# Pick the best solution out of the list of solutions
def best_sol(list_sol):
    return min(range(len(list_sol)), key=list_sol.__getitem__)

# Hill climbing algorithm
def hc(points, data = None):
    r = Route(points, data)
    steps = 0

    improvement = True
    while improvement:
        improvement = False
        #print(r.data) # For part C

        # Iterate through all possible swaps
        for i in range(len(points) - 1):
            for k in range(i + 1, len(points) - 1):

                # Calculate the new cost
                new_route = r.swap_at(i, k)
                new_distance = r.distance(new_route)
                
                '''
                Note: We don't have to pick the best neighbour as the solution space is euclidean
                such that all distance are preservered. Not picking the best neighbour and picking the 
                best neighbour will produce exactly the same result.
                '''
                #print("Swap i,k: ", i, k, " gives delta: ", r.dist - new_distance, "\\\\") # For part C

                # If the new cost is better than the old cost, set the new route
                if new_distance < r.dist:
                    r.set_route(new_route, new_distance)
                    steps += 1
                    improvement = True
                    break

            if improvement:
                break
    
    # Return the best solution
    return [r.dist, r.data, steps]

# Hill climbing with sideways moves and tabu list
def hc_tabu(points, data = None):
    r = Route(points, data)
    tabu = TabuList(100)
    sideways = 100
    steps = 0

    improvement = True
    while improvement:
        improvement = False

        # Iterate through all possible swaps
        for i in range(len(points) - 1):
            for k in range(i + 1, len(points) - 1):

                # Calculate the new cost
                new_route = r.swap_at(i, k)
                new_distance = r.distance(new_route)

                '''
                Note: We don't have to pick the best neighbour as the solution space is euclidean
                such that all distance are preservered. Not picking the best neighbour and picking the 
                best neighbour will produce exactly the same result.
                '''

                # If the new cost is better than the old cost, set the new route
                if new_distance < r.dist:
                    r.set_route(new_route, new_distance)
                    steps += 1
                    improvement = True
                    sideways = 100
                    break

                # If the neighbour is exactly the same, then make the sideways move
                elif new_distance < (r.dist + 0.001):
                    if (sideways != 0 and tabu.check_and_add(new_route)):
                        r.set_route(new_route, new_distance)
                        steps += 1
                        improvement = True
                        sideways -= 1

            if improvement:
                break
    
    # Return the best route
    return [r.dist, r.data, steps]

# Hill Climbing with random restarts
def hc_random_restart(points, max_restarts):
    list_sol = []
    num = 0

    # Continue running hill climbing max_restart times
    while num < max_restarts:
        list_sol.append(hc(points))
        num += 1

    # Find and return the best solution
    min_idx = best_sol(list_sol)

    return list_sol[min_idx]

# Unit tests
if __name__ == "__main__":
    points = generatedata.parsefile(14,1)

    shared_data = [point[0] for point in points[1:]]
    random.shuffle(shared_data)

    shared_data2 = copy.deepcopy(shared_data)

    print(hc(points, shared_data))
    print(hc_tabu(points, shared_data2))

    print(hc_random_restart(points, 100))



    



