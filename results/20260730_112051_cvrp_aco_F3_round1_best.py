# Best Round 1 implementation for update_pheromone
# Strategy ID: F3
# Winner: P2
# Best cost: 90.988227
# P1 cost: 91.695404
# P2 cost: 90.988227

import numpy as np

def update_pheromone(pheromone, solutions, costs, iteration, n_iterations):
    decay = 0.8 ** (iteration / n_iterations)  # More aggressive decay
    pheromone *= decay
    min_pheromone = 1e-10

    for i, solution in enumerate(solutions):
        cost = costs[i]
        deposit = 1.0 / (cost + 1e-10)  # Avoid div by zero
        for route in solution:
            for j in range(len(route) - 1):
                pheromone[route[j], route[j + 1]] += deposit
            pheromone[0, route[0]] += deposit  # Direct depot to first
            pheromone[route[-1], 0] += deposit  # Last to depot

    pheromone = np.maximum(pheromone, min_pheromone)
    return pheromone