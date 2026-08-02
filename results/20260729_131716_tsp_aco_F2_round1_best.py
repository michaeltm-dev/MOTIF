# Best Round 1 implementation for compute_probabilities
# Strategy ID: F2
# Winner: P2
# Best cost: 29.139440
# P1 cost: 29.194931
# P2 cost: 29.139440

import numpy as np

def compute_probabilities(
    pheromone: np.ndarray,
    heuristic: np.ndarray,
    iteration: int,
    n_iterations: int
) -> np.ndarray:
    alpha = 1.0 + (0.3 * (iteration / n_iterations))  # Encourage exploration initially
    beta = 1.0 + (0.7 * (1 - iteration / n_iterations))  # Steady exploration later
    weights = np.power(pheromone, alpha) * np.power(heuristic, beta)
    weights += 1e-10  # Numerical stability
    return weights / np.sum(weights)  # Normalize