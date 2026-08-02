# Best Round 1 implementation for initialize
# Strategy ID: F1
# Winner: P1
# Best cost: 29.179447
# P1 cost: 29.179447
# P2 cost: 29.281488

import numpy as np

def initialize(distances: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    n = distances.shape[0]
    inverse_distances = 1.0 / (distances + 1e-10)
    connectivity = np.sum(distances < np.inf, axis=1)
    heuristic = (inverse_distances * connectivity[:, np.newaxis])**2
    pheromone = np.ones_like(distances) * np.mean(connectivity)
    return heuristic, pheromone