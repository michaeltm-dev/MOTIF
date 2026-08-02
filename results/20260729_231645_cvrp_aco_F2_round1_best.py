# Best Round 1 implementation for compute_probabilities
# Strategy ID: F2
# Winner: P1
# Best cost: 90.499458
# P1 cost: 90.499458
# P2 cost: 90.499458

import numpy as np

def compute_probabilities(pheromone, heuristic, iteration, n_iterations):
    alpha = 1.0  # Pheromone influence
    beta = 3.0    # Heuristic influence
    decay = np.exp(-iteration / (n_iterations + 1))  # Exponential decay
    adjusted_pheromone = pheromone * decay
    exploration_scaling = 1 + np.log(iteration + 2)
    adjusted_heuristic = heuristic / exploration_scaling  # Log scaling for exploration
    probabilities = np.power(adjusted_pheromone, alpha) * np.power(adjusted_heuristic, beta)
    probabilities /= np.sum(probabilities)  # Normalize probabilities
    return probabilities