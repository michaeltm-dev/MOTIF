import numpy as np

def item_badness(item_idx: int, permutation: list[int], demands: np.ndarray, capacity: int) -> float:
    item = permutation[item_idx]
    
    # Super simple: larger items are worse (harder to place)
    return demands[item] / capacity