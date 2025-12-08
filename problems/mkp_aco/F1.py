import numpy as np

def initialize(prize: np.ndarray, weight: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """
    Initialize heuristic and pheromone matrices for Multiple Knapsack Problem.
    
    Parameters
    ----------
    prize : np.ndarray, shape (n,)
        Prize values for each item.
    weight : np.ndarray, shape (n, m)
        Weight matrix for each item across m constraints.
        
    Returns
    -------
    tuple[np.ndarray, np.ndarray]
        heuristic : np.ndarray, shape (n,)
            Heuristic values for each item based on prize-to-weight ratio.
        pheromone : np.ndarray, shape (n,)
            Initial pheromone levels.
    """
    # Calculate heuristic as prize-to-weight ratio
    heuristic = prize / np.sum(weight, axis=1)
    
    # Initialize pheromone trail uniformly
    pheromone = np.ones(prize.shape[0])
    
    return heuristic, pheromone