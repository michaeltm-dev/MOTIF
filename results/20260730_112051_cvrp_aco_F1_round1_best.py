# Best Round 1 implementation for initialize
# Strategy ID: F1
# Winner: P2
# Best cost: 91.753621
# P1 cost: 91.756332
# P2 cost: 91.753621

import numpy as np

def initialize(distances, demands, coords, capacity):
    n = len(demands)
    heuristic = np.zeros((n, n))
    for i in range(n):
        for j in range(1, n):  # Customers only
            if demands[j] <= capacity:
                dist_term = 1.0 / (distances[i, j] + 1e-6)
                capacity_factor = (capacity - demands[j]) / capacity
                diversity_penalty = 1.0 / np.log(1 + np.sum(demands[1:]))
                heuristic[i, j] = capacity_factor * dist_term * diversity_penalty * (1 + np.log(1 + demands[j]))
    pheromone = np.ones_like(distances)
    return heuristic, pheromone