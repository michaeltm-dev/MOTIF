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
    alpha = 1.0 + (0.6 * iteration / n_iterations)
    beta = 1.0 + (1.4 * (1 - iteration / n_iterations))
    transition_weights = (pheromone ** alpha) * (heuristic ** beta)
    transition_weights = np.clip(transition_weights, 1e-10, None)
    return transition_weights / (np.sum(transition_weights) + 1e-10)