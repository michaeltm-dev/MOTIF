# Final Round optimized implementation for initialize
# Strategy ID: F1
# Phase: Final Round (system-aware)

import numpy as np

def initialize(distances: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    n = distances.shape[0]
    inverse_distances = 1.0 / (distances + 1e-10)
    connectivity = np.sum(distances < np.inf, axis=1)
    heuristic = (inverse_distances * connectivity[:, np.newaxis])**2
    pheromone = np.ones_like(distances) * np.mean(connectivity)
    return heuristic, pheromone