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
    decay = 0.85 * (1 - iteration / n_iterations)
    pheromone *= decay

    max_pheromone = 1e3
    n_cities, n_ants = paths.shape
    for ant in range(n_ants):
        tour = paths[:, ant]
        deposit = 1.0 / costs[ant] ** 1.5  # Weight short tours more
        for i in range(n_cities):
            c = tour[i]
            n = tour[(i + 1) % n_cities]
            pheromone[c, n] += deposit
            pheromone[n, c] += deposit

    pheromone = np.clip(pheromone, 0, max_pheromone)
    return pheromone