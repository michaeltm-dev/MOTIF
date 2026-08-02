# Best Round 1 implementation for compute_probabilities
# Strategy ID: F2
# Winner: P2
# Best cost: 89.961676
# P1 cost: 90.724915
# P2 cost: 89.961676

import numpy as np

def compute_probabilities(pheromone, heuristic, iteration, n_iterations):
    alpha = 1.5 * (1 - iteration / n_iterations)  # High initial influence, tapering off
    beta = 2.5 - (1.5 * iteration / n_iterations)  # Strong heuristic influence, decreasing
    decay = 0.9 + 0.1 * (iteration / n_iterations)  # Gradual increase in pheromone decay
    pheromone_adjusted = pheromone * decay
    probabilities = np.power(pheromone_adjusted, alpha) * np.power(heuristic, beta)
    probabilities /= np.sum(probabilities)  # Normalize probabilities
    return probabilities