# Final Round optimized implementation for update_pheromone
# Strategy ID: F3
# Phase: Final Round (system-aware)

import numpy as np

def update_pheromone(
    pheromone: np.ndarray,
    paths: np.ndarray,
    costs: np.ndarray,
    iteration: int,
    n_iterations: int,
) -> np.ndarray:
    decay = 0.85 ** (iteration / n_iterations) 
    pheromone *= decay
    best_cost = np.min(costs)
    for ant in range(paths.shape[1]):
        tour = paths[:, ant]
        deposit = (1.0 / costs[ant]) * (1 + (best_cost - costs[ant]) / best_cost) ** 1.75
        for i in range(paths.shape[0]):
            c = tour[i]
            n = tour[(i + 1) % paths.shape[0]]
            pheromone[c, n] += deposit
            pheromone[n, c] += deposit
    return pheromone