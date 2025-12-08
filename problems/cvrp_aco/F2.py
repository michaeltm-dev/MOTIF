import numpy as np

def compute_probabilities(pheromone, heuristic, iteration, n_iterations):
    """
    Compute transition probabilities for CVRP considering capacity constraints.
    
    Parameters
    ----------
    pheromone : np.ndarray, shape (n, n)
        Current pheromone levels.
    heuristic : np.ndarray, shape (n, n)
        Heuristic desirability matrix.
    iteration : int
        Current iteration number.
    n_iterations : int
        Total number of iterations.
        
    Returns
    -------
    np.ndarray, shape (n, n)
        Transition probabilities matrix.
    """
    # Basic ACO probability computation
    alpha = 1.0  # Pheromone influence
    beta = 2.0   # Heuristic influence
    
    # Compute basic probabilities
    probabilities = np.power(pheromone, alpha) * np.power(heuristic, beta)
    
    return probabilities