import random
import matplotlib.pyplot as plt
import numpy as numpy
import string

def randomSolution(tsp):
    cities = list(range(len(tsp)))
    solution = []
    
    for i in range(len(tsp)):
        randomCity = cities[random.randint(0,len(cities)-1)]
        solution.append(randomCity)
        cities.remove(randomCity)
    
    return solution

def getRouteLength(tsp,solution):
    length_route = 0
    for i in range(len(solution)):
        length_route += tsp[solution[i - 1]][solution[i]]
    return length_route

def getNeighbors(solution):
    neighbors = []
    for i in range(len(solution)):
        for j in range(i+1,len(solution)):
            neighbor = solution.copy()
            neighbor[i] = solution[j]
            neighbor[j] = solution[i]
            neighbors.append(neighbor)
    return neighbors

def getBestNeighbor(tsp,neighbors):
    best_length_route = getRouteLength(tsp,neighbors[0])
    best_neighbor = neighbors[0]

    for nei in neighbors:
        current_route_length = getRouteLength(tsp,nei)
        if current_route_length < best_length_route:
            best_length_route = current_route_length
            best_neighbor = nei
    return best_neighbor,best_length_route

def hillClimbing(tsp):
    current_solution = randomSolution(tsp)
    current_route_length = getRouteLength(tsp,current_solution)
    neighbors = getNeighbors(current_solution)
    best_neighbor,best_neighbor_route_length = getBestNeighbor(tsp,neighbors)

    while best_neighbor_route_length <  current_route_length:
        current_solution = best_neighbor
        neighbors = getBestNeighbor(tsp,current_solution)
        best_neighbor,best_neighbor_route_length = getBestNeighbor(tsp,neighbors)
    return current_solution,current_route_length
        
def ProblemGenerator(nCities):
    tsp = []
    for i in range(nCities):
        dists = []
        for j in range(nCities):
            if j==i:
                dists.append(0)
            elif j<i:
                dists.append(tsp[j][i])
            else:
                dists.append(random(10,1000))
        tsp.append(dists)
    return tsp

def main():
    tsp = [
        [0, 400, 500, 300],
        [400, 0, 300, 500],
        [500, 300, 0, 400],
        [300, 500, 400, 0]
    ]

    print(hillClimbing(tsp))

if __name__ == "__main__":
    main()