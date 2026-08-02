# Final Round optimized implementation for compute_probabilities
# Strategy ID: F2
# Phase: Final Round (system-aware)

import numpy as np

def compute_probabilities(pheromone, heuristic, iteration, n_iterations):
    alpha = 1.0 + (n_iterations - iteration) / n_iterations  # Dynamic pheromone influence
    beta = 2.0  # Constant heuristic influence
    probabilities = np.power(pheromone, alpha) * np.power(heuristic, beta)
    probabilities /= np.sum(probabilities)  # Normalize probabilities
    return probabilities
