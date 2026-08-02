# Best Round 1 implementation for update_pheromone
# Strategy ID: F3
# Winner: P2
# Best cost: 28.886650
# P1 cost: 28.946408
# P2 cost: 28.886650

import numpy as np

def update_pheromone(
    pheromone: np.ndarray,
    paths: np.ndarray,
    costs: np.ndarray,
    iteration: int,
    n_iterations: int,
) -> np.ndarray:
    decay = 0.9 - 0.7 * (iteration / n_iterations)**2
    pheromone *= decay
    pheromone = np.clip(pheromone, 1e-10, None)

    n_cities, n_ants = paths.shape
    best_cost = np.min(costs)
    deposition_factor = 1.5  # Adjusted for desired reinforcement
    for ant in range(n_ants):
        tour = paths[:, ant]
        deposit = deposition_factor * (best_cost / costs[ant])**1.5
        for i in range(n_cities):
            c = tour[i]
            n = tour[(i + 1) % n_cities]
            pheromone[c, n] += deposit
            pheromone[n, c] += deposit
    return pheromone
