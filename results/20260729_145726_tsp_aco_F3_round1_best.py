# Best Round 1 implementation for update_pheromone
# Strategy ID: F3
# Winner: P2
# Best cost: 28.884722
# P1 cost: 28.929009
# P2 cost: 28.884722

import numpy as np

def update_pheromone(
    pheromone: np.ndarray,
    paths: np.ndarray,
    costs: np.ndarray,
    iteration: int,
    n_iterations: int,
) -> np.ndarray:
    decay = 0.9 ** (iteration / n_iterations) 
    pheromone *= decay
    best_cost = np.min(costs)
    for ant in range(paths.shape[1]):
        tour = paths[:, ant]
        deposit = (1.0 / costs[ant]) * (1 + (best_cost - costs[ant]) / best_cost) ** 1.5
        for i in range(paths.shape[0]):
            c = tour[i]
            n = tour[(i + 1) % paths.shape[0]]
            pheromone[c, n] += deposit
            pheromone[n, c] += deposit
    return pheromone