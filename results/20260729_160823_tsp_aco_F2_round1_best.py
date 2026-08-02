# Best Round 1 implementation for compute_probabilities
# Strategy ID: F2
# Winner: P2
# Best cost: 29.075035
# P1 cost: 29.294984
# P2 cost: 29.075035

import numpy as np

def compute_probabilities(
    pheromone: np.ndarray,
    heuristic: np.ndarray,
    iteration: int,
    n_iterations: int
) -> np.ndarray:
    alpha = 2.0 * np.exp(-iteration / n_iterations)  # Non-linear decay for pheromone influence
    beta = 1.0 / (1.0 + np.exp(-6.0 * (iteration / n_iterations - 0.5)))  # Sigmoid boost for heuristic influence
    transition_weights = np.nan_to_num(np.power(pheromone, alpha) * np.power(heuristic, beta))
    return transition_weights