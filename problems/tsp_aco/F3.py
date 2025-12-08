import numpy as np

def update_pheromone(
    pheromone: np.ndarray,
    paths: np.ndarray,
    costs: np.ndarray,
    iteration: int,
    n_iterations: int,
) -> np.ndarray:
    """
    Simulate pheromone dynamics: apply evaporation and reinforce edges used by ants.
    Shorter tours contribute more pheromone, guiding future searches.

    Parameters
    ----------
    pheromone : np.ndarray, shape (n_cities, n_cities)
        Current pheromone distribution.
    paths : np.ndarray, shape (n_cities, n_ants)
        Ant tour sequences of city indices per column.
    costs : np.ndarray, shape (n_ants,)
        Total tour cost for each ant.
    iteration : int
        Index of the current iteration.
    n_iterations : int
        Total number of iterations for adaptive tuning.

    Returns
    -------
    np.ndarray, shape (n_cities, n_cities)
        Updated pheromone levels after evaporation and deposition.
    """
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