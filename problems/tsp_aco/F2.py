import numpy as np

def compute_probabilities(
    pheromone: np.ndarray,
    heuristic: np.ndarray,
    iteration: int,
    n_iterations: int
) -> np.ndarray:
    """
    Generate unnormalized transition weights reflecting pheromone intensity and heuristic desirability.
    These weights determine the likelihood of ants moving between cities.

    Parameters
    ----------
    pheromone : np.ndarray, shape (n_cities, n_cities)
        Current pheromone levels on edges.
    heuristic : np.ndarray, shape (n_cities, n_cities)
        Heuristic desirability of edges.
    iteration : int
        Index of the current iteration.
    n_iterations : int
        Total number of iterations for adaptive tuning.

    Returns
    -------
    np.ndarray, shape (n_cities, n_cities)
        Unnormalized transition weights for ant decisions.
    """
    # Example static parameters; consider tuning externally
    alpha = 1.0  # pheromone influence
    beta = 1.0   # heuristic influence
    return np.power(pheromone, alpha) * np.power(heuristic, beta)