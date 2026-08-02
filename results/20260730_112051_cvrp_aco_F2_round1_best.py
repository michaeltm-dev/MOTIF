# Best Round 1 implementation for compute_probabilities
# Strategy ID: F2
# Winner: P1
# Best cost: 91.857570
# P1 cost: 91.857570
# P2 cost: 92.148522

import numpy as np

def compute_probabilities(pheromone, heuristic, iteration, n_iterations):
    alpha = 1.0 + 0.3 * (n_iterations - iteration) / n_iterations
    beta = 2.0
    decay_factor = 0.9 ** (iteration / n_iterations)
    probabilities = decay_factor * np.power(pheromone, alpha) * np.power(heuristic, beta)
    return probabilities / np.sum(probabilities)