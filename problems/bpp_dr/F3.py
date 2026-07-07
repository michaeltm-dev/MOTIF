import numpy as np

def insert_position(item: int, permutation: list[int], demands: np.ndarray, capacity: int) -> int:
    if len(permutation) == 0:
        return 0
    
    # Super simple: insert next to smallest item (most likely to fit together)
    smallest_item_idx = 0
    smallest_size = demands[permutation[0]]
    
    for i, perm_item in enumerate(permutation):
        if demands[perm_item] < smallest_size:
            smallest_size = demands[perm_item]
            smallest_item_idx = i
    
    # Insert after the smallest item
    return smallest_item_idx + 1