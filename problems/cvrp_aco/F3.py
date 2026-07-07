import numpy as np

def update_pheromone(pheromone, solutions, costs, iteration, n_iterations):
    # Evaporation
    decay = 0.9
    pheromone = pheromone * decay
    
    # Deposit pheromone
    for i, solution in enumerate(solutions):
        cost = costs[i]
        deposit = 1.0 / cost  # Better solutions deposit more pheromone
        
        # Deposit on all edges in the solution
        for route in solution:
            for j in range(len(route) - 1):
                pheromone[route[j], route[j + 1]] += deposit
    
    # Ensure minimum pheromone level
    pheromone = np.maximum(pheromone, 1e-10)
    
    return pheromone