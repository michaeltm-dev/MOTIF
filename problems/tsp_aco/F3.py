import numpy as np

def update_pheromone(
    pheromone: np.ndarray,
    paths: np.ndarray,
    costs: np.ndarray,
    iteration: int,
    n_iterations: int,
) -> np.ndarray:
    # Decay factor
    decay = 0.9

    # Evaporation
    pheromone *= decay

    n_cities, n_ants = paths.shape
    # Deposit pheromone: shorter tours deposit more
    for ant in range(n_ants):
        tour = paths[:, ant]
        deposit = 1.0 / costs[ant]
        for i in range(n_cities):
            c = tour[i]
            n = tour[(i + 1) % n_cities]
            pheromone[c, n] += deposit
            pheromone[n, c] += deposit

    return pheromone