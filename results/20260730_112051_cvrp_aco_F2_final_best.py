# Final Round optimized implementation for compute_probabilities
# Strategy ID: F2
# Phase: Final Round (system-aware)

import numpy as np

def compute_probabilities(pheromone, heuristic, iteration, n_iterations):
    alpha = 1.0 + 0.3 * (n_iterations - iteration) / n_iterations
    beta = 2.0
    decay_factor = 0.9 ** (iteration / n_iterations)
    probabilities = decay_factor * np.power(pheromone, alpha) * np.power(heuristic, beta)
    return probabilities / np.sum(probabilities)