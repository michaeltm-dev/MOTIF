# Best Round 1 implementation for initialize
# Strategy ID: F1
# Winner: P1
# Best cost: 89.961676
# P1 cost: 89.961676
# P2 cost: 89.961676

import numpy as np

def initialize(distances, demands, coords, capacity):
    n = len(demands)
    distances = np.where(distances == 0, np.inf, distances)
    heuristic = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                demand_weight = demands[j] / capacity
                spatial_factor = np.exp(-np.linalg.norm(coords[i] - coords[j]))
                heuristic[i][j] = (1.0 / distances[i][j]) * (1 + demand_weight) * spatial_factor
            else:
                heuristic[i][j] = 0
    pheromone = np.ones_like(distances)
    return heuristic, pheromone