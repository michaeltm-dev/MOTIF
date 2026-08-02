# Best Round 1 implementation for compute_probabilities
# Strategy ID: F2
# Winner: P2
# Best cost: 28.819478
# P1 cost: 29.075606
# P2 cost: 28.819478

import numpy as np

def compute_probabilities(
    pheromone: np.ndarray,
    heuristic: np.ndarray,
    iteration: int,
    n_iterations: int
) -> np.ndarray:
    alpha = 1.0 + (iteration / n_iterations) ** 1.5 * 1.5  # Modified exponent
    beta = 1.0 + (1.0 - (iteration / n_iterations)) ** 1.5 * 1.5  # Modified exponent
    transition_weights = np.power(pheromone, alpha) * np.power(heuristic, beta)
    transition_weights = np.log1p(transition_weights)  # Logarithmic scaling for stability
    transition_weights /= np.max(transition_weights)  # Maximum scaling for stability
    return transition_weights / np.sum(transition_weights)  # Normalize