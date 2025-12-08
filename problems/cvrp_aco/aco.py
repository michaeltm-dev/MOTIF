import numpy as np
from F1 import initialize
from F2 import compute_probabilities
from F3 import update_pheromone

def construct_solutions(
    distances, demands, heuristic, pheromone, capacity, n_ants, iteration, n_iterations
):
    """
    Construct solutions for all ants using ACO for CVRP.
    Optimized version for better performance.
    """
    n_nodes = distances.shape[0]
    solutions = []
    
    # Pre-compute probabilities once per iteration instead of per node selection
    probabilities = compute_probabilities(pheromone, heuristic, iteration, n_iterations)
    
    # Pre-allocate arrays for better memory management
    demands_array = np.asarray(demands)
    
    for ant in range(n_ants):
        solution = []
        current_route = [0]  # Start at depot
        current_capacity = capacity
        current_node = 0
        
        # Use numpy boolean array instead of set for faster operations
        unvisited = np.ones(n_nodes, dtype=bool)
        unvisited[0] = False  # Depot already visited
        
        while np.any(unvisited):
            # Vectorized feasibility check
            feasible_mask = unvisited & (demands_array <= current_capacity)
            feasible_indices = np.where(feasible_mask)[0]
            
            if len(feasible_indices) == 0:
                # Return to depot, start new route
                current_route.append(0)
                solution.append(current_route)
                current_route = [0]
                current_capacity = capacity
                current_node = 0
                continue
            
            # Vectorized probability extraction and normalization
            node_probs = probabilities[current_node, feasible_indices]
            total_prob = np.sum(node_probs)
            
            if total_prob == 0:
                next_node = np.random.choice(feasible_indices)
            else:
                # Normalize and select
                normalized_probs = node_probs / total_prob
                next_node = np.random.choice(feasible_indices, p=normalized_probs)
            
            # Update state
            current_route.append(next_node)
            current_capacity -= demands_array[next_node]
            current_node = next_node
            unvisited[next_node] = False
        
        # Close last route if needed
        if len(current_route) > 1:
            current_route.append(0)
            solution.append(current_route)
        
        solutions.append(solution)
    
    return solutions

def calculate_solution_cost(solution, distances):
    """
    Calculate total cost of a solution.
    Optimized with vectorized operations where possible.
    """
    total_cost = 0.0
    for route in solution:
        if len(route) > 1:
            # Vectorized cost calculation for route
            route_array = np.array(route)
            route_costs = distances[route_array[:-1], route_array[1:]]
            total_cost += np.sum(route_costs)
    return total_cost

def run_cvrp_aco(distances, demands, coords, capacity, n_ants=50, n_iterations=100, seed=0):
    """
    Run ACO for CVRP.
    Optimized version with reduced function calls and better memory usage.
    """
    # Ensure minimum distance values
    distances = np.maximum(distances, 1e-6)

    # Initialize heuristic and pheromone once
    heuristic, pheromone = initialize(distances.copy(), demands.copy(), coords.copy(), capacity)

    # Ensure heuristic and pheromone are finite and non-negative
    heuristic = np.nan_to_num(heuristic, nan=0.01, posinf=1.0, neginf=0.01)
    pheromone = np.nan_to_num(pheromone, nan=0.01, posinf=1.0, neginf=0.01)
    
    # Ensure minimum positive values
    heuristic = np.maximum(heuristic, 0.01)
    pheromone = np.maximum(pheromone, 0.01)
    
    best_cost = float('inf')
    best_solution = None
    
    # Pre-allocate arrays
    costs = np.zeros(n_ants)

    np.random.seed(seed)
    
    for iteration in range(n_iterations):
        # Generate solutions
        solutions = construct_solutions(
            distances, demands, heuristic, pheromone, capacity, n_ants, iteration, n_iterations
        )
        
        # Vectorized cost calculation where possible
        for i, solution in enumerate(solutions):
            costs[i] = calculate_solution_cost(solution, distances)
        
        # Update best solution
        min_idx = np.argmin(costs)
        min_cost = costs[min_idx]
        if min_cost < best_cost:
            best_cost = min_cost
            best_solution = solutions[min_idx]
        
        # Update pheromone using F3
        pheromone = update_pheromone(pheromone, solutions, costs.tolist(), iteration, n_iterations)

        pheromone = np.nan_to_num(pheromone, nan=0.01, posinf=1.0, neginf=0.01)
        pheromone = np.maximum(pheromone, 0.01)  # Ensure minimum
    
    return best_cost