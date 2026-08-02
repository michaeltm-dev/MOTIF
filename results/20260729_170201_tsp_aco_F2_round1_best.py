# Best Round 1 implementation for compute_probabilities
# Strategy ID: F2
# Winner: P2
# Best cost: 28.893480
# P1 cost: 28.966099
# P2 cost: 28.893480

import numpy as np

def compute_probabilities(
    pheromone: np.ndarray,
    heuristic: np.ndarray,
    iteration: int,
    n_iterations: int
) -> np.ndarray:
    alpha = 1.0 + (0.9 * (iteration / n_iterations))
    beta = 1.0 + (0.9 * (1 - iteration / n_iterations))
    weights = np.power(pheromone, alpha) * np.power(heuristic, beta)
    epsilon = 1e-10
    return weights / (np.sum(weights) + epsilon)