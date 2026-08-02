# Final Round optimized implementation for initialize
# Strategy ID: F1
# Phase: Final Round (system-aware)

import numpy as np

def initialize(distances: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    min_distances = np.min(distances, axis=1).reshape(-1, 1)
    heuristic = (1.0 / (distances + 1e-10)) * (min_distances / (distances + 1e-10))  
    pheromone = np.ones_like(distances) * 0.5
    return heuristic, pheromone