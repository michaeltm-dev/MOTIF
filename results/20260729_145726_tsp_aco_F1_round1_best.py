# Best Round 1 implementation for initialize
# Strategy ID: F1
# Winner: P2
# Best cost: 28.907365
# P1 cost: 28.929009
# P2 cost: 28.907365

import numpy as np

def initialize(distances: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    avg_distance = np.mean(distances[distances > 0])
    proximity = (avg_distance - distances) / (avg_distance + 1e-10)
    heuristic = (1.0 / distances) * np.clip(proximity, 0, 1)
    connectivity = np.count_nonzero(distances, axis=1)
    pheromone = np.ones_like(distances) / (connectivity + 1e-10)
    return heuristic, pheromone