# Final Round optimized implementation for initialize
# Strategy ID: F1
# Phase: Final Round (system-aware)

import numpy as np

def initialize(distances, demands, coords, capacity):
    n = len(demands)
    heuristic = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                load_factor = demands[j] / capacity
                proximity_effect = np.exp(-np.linalg.norm(coords[i] - coords[j]) / np.sqrt(2))
                saturation_penalty = np.exp(-max(0, load_factor - 1)**2)
                heuristic[i, j] = (1.0 / distances[i, j]) * saturation_penalty * proximity_effect
    pheromone = np.ones_like(distances)
    return heuristic, pheromone