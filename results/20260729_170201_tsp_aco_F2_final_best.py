# Final Round optimized implementation for compute_probabilities
# Strategy ID: F2
# Phase: Final Round (system-aware)

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