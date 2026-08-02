# Final Round optimized implementation for initialize
# Strategy ID: F1
# Phase: Final Round (system-aware)

import numpy as np

def initialize(distances: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    avg_distance = np.mean(distances[distances > 0])
    proximity = (avg_distance - distances) / (avg_distance + 1e-10)
    heuristic = (1.0 / distances) * np.clip(proximity, 0, 1)
    connectivity = np.count_nonzero(distances, axis=1)
    pheromone = np.ones_like(distances) / (connectivity + 1e-10)
    return heuristic, pheromone