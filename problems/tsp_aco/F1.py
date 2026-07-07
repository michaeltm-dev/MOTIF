import numpy as np

def initialize(distances: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    heuristic = 1.0 / distances
    pheromone = np.ones_like(distances)  # Initialize pheromone levels uniformly
    return heuristic, pheromone
