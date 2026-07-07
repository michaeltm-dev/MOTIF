import numpy as np

def compute_probabilities(
    pheromone: np.ndarray,
    heuristic: np.ndarray,
    iteration: int,
    n_iterations: int
) -> np.ndarray:
    # Static parameters (can be tuned)
    alpha = 1.0  # pheromone influence
    beta = 2.0   # heuristic influence
    
    # Calculate unnormalized probabilities
    probabilities = np.power(pheromone, alpha) * np.power(heuristic, beta)
    
    return probabilities