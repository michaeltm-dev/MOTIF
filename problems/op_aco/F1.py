import numpy as np

def initialize(prize: np.ndarray, distance: np.ndarray, maxlen: float) -> tuple[np.ndarray, np.ndarray]:
    """
    Initialize heuristic and pheromone matrices for Orienteering Problem.
    
    Parameters
    ----------
    prize : np.ndarray, shape (n,)
        Prize values for each node.
    distance : np.ndarray, shape (n, n)
        Distance matrix between nodes.
    maxlen : float
        Maximum allowed tour length.
        
    Returns
    -------
    tuple[np.ndarray, np.ndarray]
        heuristic : np.ndarray, shape (n, n)
            Heuristic values for transitions between nodes.
        pheromone : np.ndarray, shape (n, n)
            Initial pheromone levels.
    """
    # Create heuristic matrix based on prize-to-distance ratio
    heuristic = prize[np.newaxis, :] / distance # heuristic[i, j] = prize[j] / distance[i, j]
    
    # Create initial pheromone matrix with uniform values
    pheromone = np.ones_like(distance)
    
    return heuristic, pheromone