# Best Round 1 implementation for update_pheromone
# Strategy ID: F3
# Winner: P2
# Best cost: 28.973914
# P1 cost: 29.039832
# P2 cost: 28.973914

import numpy as np

def update_pheromone(
    pheromone: np.ndarray,
    paths: np.ndarray,
    costs: np.ndarray,
    iteration: int,
    n_iterations: int,
) -> np.ndarray:
    decay = 0.85 * (1 - (iteration / n_iterations) ** 2)
    pheromone *= decay
    n_cities, n_ants = paths.shape
    best_cost = np.min(costs)
    strong_deposit = 1.0 / (best_cost + 1e-10)
    weak_deposit_factor = 0.1
    for ant in range(n_ants):
        deposit = strong_deposit if costs[ant] == best_cost else weak_deposit_factor * (1.0 / (costs[ant] + 1e-10))
        tour = paths[:, ant]
        for i in range(n_cities):
            c = tour[i]
            n = tour[(i + 1) % n_cities]
            pheromone[c, n] += deposit
            pheromone[n, c] += deposit
    return pheromone
