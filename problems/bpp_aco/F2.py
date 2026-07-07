import numpy as np

def update_pheromone(pheromone: np.ndarray, paths: list, fitnesses: np.ndarray, iteration: int, n_iterations: int) -> np.ndarray:
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