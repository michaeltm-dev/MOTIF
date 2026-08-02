# Best Round 1 implementation for update_pheromone
# Strategy ID: F3
# Winner: P1
# Best cost: 92.766908
# P1 cost: 92.766908
# P2 cost: 92.766908

import numpy as np

def update_pheromone(pheromone, solutions, costs, iteration, n_iterations):
    decay = 0.85 * (1 - iteration / n_iterations)  # Higher decay to encourage exploration
    pheromone *= decay
    route_count = np.zeros(pheromone.shape)  # Count for each edge

    for i, solution in enumerate(solutions):
        cost = costs[i]
        deposit = 1.0 / cost
        for route in solution:
            for j in range(len(route) - 1):
                pheromone[route[j], route[j + 1]] += deposit
                route_count[route[j], route[j + 1]] += 1

    # Adaptive deposition: increase heavy use if underutilized
    for i in range(pheromone.shape[0]):
        for j in range(pheromone.shape[1]):
            if route_count[i, j] > 0:
                pheromone[i, j] += deposit / route_count[i, j]  # Normalize by usage count

    pheromone = np.clip(pheromone, 1e-10, None)  # Stability
    return pheromone