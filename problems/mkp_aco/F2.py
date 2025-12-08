import numpy as np

def compute_probabilities(
    pheromone: np.ndarray,
    heuristic: np.ndarray,
    iteration: int,
    n_iterations: int
) -> np.ndarray:
    """
    Generate unnormalized transition weights for item selection based on pheromone and heuristic.
    
    Parameters
    ----------
    pheromone : np.ndarray, shape (n+1,)
        Current pheromone levels (including dummy node).
    heuristic : np.ndarray, shape (n+1,)
        Heuristic desirability values (including dummy node).
    iteration : int
        Current iteration number.
    n_iterations : int
        Total number of iterations.
        
    Returns
    -------
    np.ndarray, shape (n+1,)
        Unnormalized transition weights for item selection.
    """
    # Static parameters (can be tuned)
    alpha = 1.0  # pheromone influence
    beta = 2.0   # heuristic influence
    
    # Calculate unnormalized probabilities
    probabilities = np.power(pheromone, alpha) * np.power(heuristic, beta)
    
    return probabilities