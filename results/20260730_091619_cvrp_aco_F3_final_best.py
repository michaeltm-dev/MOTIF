# Final Round optimized implementation for update_pheromone
# Strategy ID: F3
# Phase: Final Round (system-aware)

import numpy as np

def update_pheromone(pheromone, solutions, costs, iteration, n_iterations):
    decay = 0.85 + 0.1 * (iteration / n_iterations)
    pheromone *= decay
    min_deposit = 1e-3
    best_cost = min(costs) + 1e-10
    avg_cost = np.mean(costs)

    for i, solution in enumerate(solutions):
        cost = costs[i]
        deposit = (best_cost / cost) ** 2 if cost < best_cost else min_deposit
        for route in solution:
            route_length = len(route)
            for j in range(route_length - 1):
                pheromone[route[j], route[j + 1]] += deposit * (1.5 if route[j] == 0 else 1.0) * (1 - (route_length / len(solutions)))

    pheromone = np.maximum(pheromone, 1e-10)
    return pheromone