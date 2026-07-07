import numpy as np

def initialize(distances, demands, coords, capacity):
    # Simple heuristic: inverse of distance
    heuristic = 1.0 / distances
    
    # Initialize pheromone uniformly
    pheromone = np.ones_like(distances)
    
    return heuristic, pheromone