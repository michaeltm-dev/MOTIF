import numpy as np

def update_pheromone(pheromone: np.ndarray, sols: list, objs: np.ndarray, it: int, n_iterations: int) -> np.ndarray:
    # Evaporation factor
    decay = 0.9 

    # Apply evaporation to all edges
    pheromone = pheromone * decay
    
    # Calculate reinforcement factor
    Q = 1.0 / np.sum(objs) 
    
    # Deposit pheromone for each ant's solution
    for i in range(len(sols)):
        sol = sols[i]
        obj = objs[i]
        
        # Update pheromone on edges in the solution
        for j in range(len(sol) - 1):
            from_node = sol[j]
            to_node = sol[j + 1]
            pheromone[from_node, to_node] += Q * obj
    
    return pheromone