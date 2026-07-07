import numpy as np

def initialize(prize: np.ndarray, weight: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    # Calculate heuristic as prize-to-weight ratio
    heuristic = prize / np.sum(weight, axis=1)
    
    # Initialize pheromone trail uniformly
    pheromone = np.ones(prize.shape[0])
    
    return heuristic, pheromone