import numpy as np

def initialize(demands: np.ndarray, capacity: int) -> tuple[np.ndarray, np.ndarray]:
    n = len(demands)
    
    # Basic heuristic: normalized demand ratios
    # Items with similar sizes are more likely to fit together efficiently
    heuristic = np.tile(demands / demands.max(), (n, 1))
    
    # Clamp values to avoid numerical issues
    heuristic = np.clip(heuristic, 1e-6, 1e6)
    
    # Normalize to [0, 1] range
    heuristic = heuristic / heuristic.max()
    heuristic = np.clip(heuristic, 1e-6, 1.0)
    
    # Initialize pheromone uniformly
    pheromone = np.ones((n, n))
    
    return heuristic, pheromone