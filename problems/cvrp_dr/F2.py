import numpy as np

def customer_badness(customer_idx: int, permutation: list[int], distances: np.ndarray, 
                    demands: np.ndarray, capacity: int) -> float:
    customer = permutation[customer_idx]
    
    # Simple badness: customers with large demands are bad
    demand_badness = demands[customer] / capacity
    
    # Add distance penalty: sum distances to all other customers in permutation
    distance_penalty = 0.0
    for other_customer in permutation:
        distance_penalty += distances[customer, other_customer]
    
    return demand_badness + distance_penalty / len(permutation)