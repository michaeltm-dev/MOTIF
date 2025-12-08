import numpy as np

def update_pheromone(pheromone: np.ndarray, paths: list, fitnesses: np.ndarray, iteration: int, n_iterations: int) -> np.ndarray:
    """
    Update pheromone levels based on bin packing solutions.
    
    This strategy manages the learning mechanism by:
    - Reducing old pheromone information (evaporation)
    - Reinforcing successful item combinations based on packing efficiency
    - Balancing memory persistence with new solution discoveries
    
    Parameters
    ----------
    pheromone : np.ndarray, shape (n, n)
        Current pheromone distribution matrix.
    paths : list[np.ndarray]
        List of ant solutions. Each solution is an array of shape (n,).
    fitnesses : np.ndarray, shape (n_ants,)
        Fitness values of solutions based on bin utilization.
    iteration : int
        Current iteration number.
    n_iterations : int
        Total number of iterations.
        
    Returns
    -------
    np.ndarray, shape (n, n)
        Updated pheromone levels after learning from solution quality.
    """
    # Hyperparameters
    decay = 0.95
    n_ants = len(paths)
    
    # Initialize delta pheromone matrix
    delta_pheromone = np.zeros_like(pheromone)
    
    # Deposit pheromone based on solution fitness
    for path, fitness in zip(paths, fitnesses):
        # Reinforce item combinations that appear in same bins
        delta_pheromone[path[:, None] == path[None, :]] += fitness / n_ants
    
    # Apply evaporation and add new pheromone
    pheromone *= decay
    pheromone += delta_pheromone
    
    return pheromone