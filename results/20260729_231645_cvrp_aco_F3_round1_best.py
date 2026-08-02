# Best Round 1 implementation for update_pheromone
# Strategy ID: F3
# Winner: P2
# Best cost: 90.499458
# P1 cost: 92.181080
# P2 cost: 90.499458

import numpy as np

def update_pheromone(pheromone, solutions, costs, iteration, n_iterations):
    decay = 0.85 + 0.15 * (iteration / n_iterations)
    pheromone *= decay
    avg_cost = np.mean(costs)
    for i, solution in enumerate(solutions):
        cost = costs[i]
        deposit = (1.0 / (cost + 1e-10)) * (1 + (np.std(costs) / (avg_cost + 1e-10)))
        for route in solution:
            for j in range(len(route) - 1):
                pheromone[route[j], route[j + 1]] += deposit
                if j == 0:
                    pheromone[route[-1], 0] += deposit
    pheromone = np.maximum(pheromone, 1e-10)
    return pheromone