import numpy as np

def insert_position(customer: int, permutation: list[int], distances: np.ndarray, 
                   demands: np.ndarray, capacity: int) -> int:
    # Simple strategy: insert next to nearest customer
    if len(permutation) == 0:
        return 0
    
    # Find nearest customer in permutation
    nearest_idx = 0
    min_distance = distances[customer, permutation[0]]
    
    for i, perm_customer in enumerate(permutation):
        dist = distances[customer, perm_customer]
        if dist < min_distance:
            min_distance = dist
            nearest_idx = i
    
    # Insert next to nearest customer (after it)
    return nearest_idx + 1