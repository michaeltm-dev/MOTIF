# Final Round optimized implementation for initialize
# Strategy ID: F1
# Phase: Final Round (system-aware)

import numpy as np

def initialize(distances, demands, coords, capacity):
    n = len(demands)
    heuristic = np.zeros((n, n))
    depot_index = 0
    for i in range(n):
        for j in range(n):
            if i != j:
                distance = distances[i, j] if distances[i, j] > 0 else np.inf
                if demands[j] <= capacity:
                    normalized_demand = demands[j] / capacity
                    capacity_pressure = 1 - normalized_demand
                    heuristic[i, j] = capacity_pressure / distance
    pheromone = np.ones((n, n))
    return heuristic, pheromone