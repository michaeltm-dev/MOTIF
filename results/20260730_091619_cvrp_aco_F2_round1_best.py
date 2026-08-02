# Best Round 1 implementation for compute_probabilities
# Strategy ID: F2
# Winner: P2
# Best cost: 87.224017
# P1 cost: 88.699351
# P2 cost: 87.224017

import numpy as np

def compute_probabilities(pheromone, heuristic, iteration, n_iterations):
    alpha = 0.8 + 0.2 * (1 - iteration / n_iterations)
    beta = 2.5 + 1.5 * (iteration / n_iterations)
    scores = np.power(pheromone, alpha) * np.power(heuristic, beta) + 1e-10
    probabilities = scores / np.sum(scores)
    return probabilities