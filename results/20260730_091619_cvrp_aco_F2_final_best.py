# Final Round optimized implementation for compute_probabilities
# Strategy ID: F2
# Phase: Final Round (system-aware)

import numpy as np

def compute_probabilities(pheromone, heuristic, iteration, n_iterations):
    alpha = 0.8 + 0.2 * (1 - iteration / n_iterations)
    beta = 2.5 + 1.5 * (iteration / n_iterations)
    scores = np.power(pheromone, alpha) * np.power(heuristic, beta) + 1e-10
    probabilities = scores / np.sum(scores)
    return probabilities