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
    decay = 0.92 * (1 - (iteration / n_iterations) ** 2)
    pheromone *= decay

    n_cities, n_ants = paths.shape
    ranked_indices = np.argsort(costs)
    for rank, ant in enumerate(ranked_indices):
        tour = paths[:, ant]
        deposit = 20 / (rank + 1) if costs[ant] > 0 else 2.0
        for i in range(n_cities):
            c = tour[i]
            n = tour[(i + 1) % n_cities]
            pheromone[c, n] += deposit
            pheromone[n, c] += deposit
    return pheromone