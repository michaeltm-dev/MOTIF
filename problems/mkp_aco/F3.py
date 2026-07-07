import numpy as np

def update_pheromone(pheromone: np.ndarray, sols: np.ndarray, objs: np.ndarray, it: int, n_iterations: int) -> np.ndarray:
    # Decay factor
    decay = 0.9

    # Evaporation
    pheromone = pheromone * decay
    
    # Deposit pheromone
    Q = 1.0 / np.sum(objs) if np.sum(objs) > 0 else 1.0
    
    for i in range(len(objs)):
        sol = sols[i]
        obj = objs[i]
        
        # Deposit pheromone on selected items
        for item in sol:
            if item < len(pheromone) - 1:  # Skip dummy node
                pheromone[item] += Q * obj
        
    return pheromone