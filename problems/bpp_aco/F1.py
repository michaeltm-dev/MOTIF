import numpy as np

def initialize(demands: np.ndarray, capacity: int) -> tuple[np.ndarray, np.ndarray]:
    """
    Initialize heuristic and pheromone matrices for Bin Packing Problem.
    
    This strategy creates the foundation for intelligent item placement by:
    - Transforming demand information into placement desirability
    - Setting initial pheromone levels for exploration guidance
    
    Parameters
    ----------
    demands : np.ndarray, shape (n,)
        Demand/size of each item to be packed.
    capacity : int
        Bin capacity constraint.
        
    Returns
    -------
    tuple[np.ndarray, np.ndarray]
        heuristic : np.ndarray, shape (n, n)
            Heuristic matrix representing desirability of item combinations.
        pheromone : np.ndarray, shape (n, n)
            Initial pheromone levels for exploration guidance.
    """
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