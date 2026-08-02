# Final Round optimized implementation for initialize
# Strategy ID: F1
# Phase: Final Round (system-aware)

import numpy as np

def initialize(distances: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    mean_distance = np.mean(distances)
    min_distance = np.min(distances)
    stability_factor = (mean_distance - distances) / (mean_distance + 1e-10)
    normalized_distances = np.linalg.norm(distances, axis=1)
    heuristic = (1.0 / (distances + 1e-10)) * stability_factor * (1.0 / (normalized_distances[:, np.newaxis] + 1e-10)) * (mean_distance - min_distance) / mean_distance
    pheromone = np.maximum(1.0 / (distances + 1e-10), 1.0) * (0.5) * (mean_distance - distances) / mean_distance
    return heuristic, pheromone
