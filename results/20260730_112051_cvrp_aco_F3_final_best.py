# Final Round optimized implementation for update_pheromone
# Strategy ID: F3
# Phase: Final Round (system-aware)

import numpy as np

def update_pheromone(pheromone, solutions, costs, iteration, n_iterations):
    decay = 0.9 ** (iteration / n_iterations)
    pheromone *= decay
    min_pheromone = 1e-10

    total_cost = np.mean(costs)
    for i, solution in enumerate(solutions):
        cost = costs[i]
        deposit = (total_cost / cost) * np.sqrt(1 + np.log(1 + cost))
        for route in solution:
            for j in range(len(route) - 1):
                pheromone[route[j], route[j + 1]] += deposit
            pheromone[0, route[0]] += deposit
            pheromone[route[-1], 0] += deposit

    pheromone = np.maximum(pheromone, min_pheromone)
    return pheromone