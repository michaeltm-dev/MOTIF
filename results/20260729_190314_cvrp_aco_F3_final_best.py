# Final Round optimized implementation for update_pheromone
# Strategy ID: F3
# Phase: Final Round (system-aware)

import numpy as np

def update_pheromone(pheromone, solutions, costs, iteration, n_iterations):
    decay = 0.87
    pheromone = pheromone * decay
    average_cost = np.mean(costs)
    alpha = 1.0 / (iteration + 1)
    for i, solution in enumerate(solutions):
        cost = costs[i]
        deposit = (3.0 / cost if cost < average_cost else 1.0 / cost) * (1 + alpha)
        for route in solution:
            for j in range(len(route) - 1):
                pheromone[route[j], route[j + 1]] += deposit
            pheromone[route[-1], 0] += deposit
    pheromone = np.maximum(pheromone, 1e-10)
    return pheromone