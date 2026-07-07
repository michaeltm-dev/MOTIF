import numpy as np

def initialize(prize: np.ndarray, distance: np.ndarray, maxlen: float) -> tuple[np.ndarray, np.ndarray]:
    # Create heuristic matrix based on prize-to-distance ratio
    heuristic = prize[np.newaxis, :] / distance # heuristic[i, j] = prize[j] / distance[i, j]
    
    # Create initial pheromone matrix with uniform values
    pheromone = np.ones_like(distance)
    
    return heuristic, pheromone