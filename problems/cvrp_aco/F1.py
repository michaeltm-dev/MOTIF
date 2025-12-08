import numpy as np

def initialize(distances, demands, coords, capacity):
    """
    Initialize heuristic and pheromone matrices for CVRP.
    
    Parameters
    ----------
    distances : np.ndarray, shape (n, n)
        Distance matrix between nodes.
    demands : np.ndarray, shape (n,)
        Demand for each node.
    coords : np.ndarray, shape (n, 2)
        Node coordinates.
    capacity : int
        Vehicle capacity.
        
    Returns
    -------
    tuple[np.ndarray, np.ndarray]
        heuristic : np.ndarray, shape (n, n)
            Heuristic desirability matrix.
        pheromone : np.ndarray, shape (n, n)
            Initial pheromone levels.
    """
    # Simple heuristic: inverse of distance
    heuristic = 1.0 / distances
    
    # Initialize pheromone uniformly
    pheromone = np.ones_like(distances)
    
    return heuristic, pheromone