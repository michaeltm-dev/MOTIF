import numpy as np

def compute_probabilities(
    pheromone: np.ndarray,
    heuristic: np.ndarray,
    iteration: int,
    n_iterations: int
) -> np.ndarray:
    # Example static parameters; consider tuning externally
    alpha = 1.0  # pheromone influence
    beta = 1.0   # heuristic influence
    return np.power(pheromone, alpha) * np.power(heuristic, beta)
