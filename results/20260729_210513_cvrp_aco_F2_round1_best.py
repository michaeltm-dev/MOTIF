# Best Round 1 implementation for compute_probabilities
# Strategy ID: F2
# Winner: P1
# Best cost: 92.035802
# P1 cost: 92.035802
# P2 cost: 92.268658

import numpy as np

def compute_probabilities(pheromone, heuristic, iteration, n_iterations):
    alpha = 1.0 + (n_iterations - iteration) / n_iterations  # Dynamic pheromone influence
    beta = 2.0  # Constant heuristic influence
    probabilities = np.power(pheromone, alpha) * np.power(heuristic, beta)
    probabilities /= np.sum(probabilities)  # Normalize probabilities
    return probabilities
