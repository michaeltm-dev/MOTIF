import numpy as np

def initialize(distances: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """
    Initialize heuristic and pheromone matrices.

    Parameters
    ----------
    distances : np.ndarray, shape (n_cities, n_cities)
        Matrix of pairwise distances between cities; entries must be positive.

    Returns
    -------
    tuple[np.ndarray, np.ndarray]
        heuristic : np.ndarray, shape (n_cities, n_cities)
            A matrix representing the desirability of traveling between cities based on local information.
        pheromone : np.ndarray, shape (n_cities, n_cities)
            A matrix representing the initial intensity of pheromone trails, which guide exploration
            based on accumulated experience.
    """
    heuristic = 1.0 / distances 
    pheromone = np.ones_like(distances)  # Initialize pheromone levels uniformly
    return heuristic, pheromone