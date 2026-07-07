import numpy as np

def edge_score(i: int, j: int, distances: np.ndarray, demands: np.ndarray, capacity: int) -> float:
    # Basic implementation: prefer short distances and small demands
    # Shorter edges get higher scores
    distance_score = -distances[i, j]
    
    # Prefer customers with smaller demands (easier to fit)
    demand_penalty = -demands[j] / capacity
    
    return distance_score + demand_penalty