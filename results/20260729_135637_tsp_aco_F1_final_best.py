# Final Round optimized implementation for initialize
# Strategy ID: F1
# Phase: Final Round (system-aware)

import numpy as np

def initialize(distances: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    max_distances = np.max(distances, axis=1)
    min_distances = np.min(distances + 1e-10, axis=1)
    heuristic = 1.0 / (distances + 1e-10) * (1.0 - distances / (max_distances[:, None] + 1e-10))
    diversity_penalty = distances / (min_distances[:, None] + 1e-10)
    adjusted_heuristic = heuristic / (1.0 + 0.6 * diversity_penalty)
    pheromone = np.ones_like(distances) * 1.0
    return adjusted_heuristic, pheromone