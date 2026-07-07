import numpy as np

def edge_score(i: int, j: int, distances: np.ndarray) -> float:
    # Simple implementation: shorter edges get higher scores
    # Negate distance so shorter = higher score
    return -distances[i, j]