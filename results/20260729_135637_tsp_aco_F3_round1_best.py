# Best Round 1 implementation for update_pheromone
# Strategy ID: F3
# Winner: P2
# Best cost: 28.828920
# P1 cost: 29.075606
# P2 cost: 28.828920

import numpy as np

def update_pheromone(
    pheromone: np.ndarray,
    paths: np.ndarray,
    costs: np.ndarray,
    iteration: int,
    n_iterations: int,
) -> np.ndarray:
    decay = 0.9 * (1 - (iteration / n_iterations) ** 2)
    pheromone *= decay

    n_cities, n_ants = paths.shape
    ranked_indices = np.argsort(costs)
    rank_factor = np.linspace(1.0, 2.0, n_ants)
    for rank, ant in enumerate(ranked_indices):
        tour = paths[:, ant]
        deposit = 10 / (rank + 1) if costs[ant] > 0 else 1.0
        for i in range(n_cities):
            c = tour[i]
            n = tour[(i + 1) % n_cities]
            pheromone[c, n] += deposit
            pheromone[n, c] += deposit
    return pheromone