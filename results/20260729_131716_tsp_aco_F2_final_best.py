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
    alpha = 1.0 + (0.3 * (iteration / n_iterations))  # Encourage exploration initially
    beta = 1.0 + (0.7 * (1 - iteration / n_iterations))  # Steady exploration later
    weights = np.power(pheromone, alpha) * np.power(heuristic, beta)
    weights += 1e-10  # Numerical stability
    return weights / np.sum(weights)  # Normalize