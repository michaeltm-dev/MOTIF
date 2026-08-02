# Final Round optimized implementation for generate_guide_matrix
# Strategy ID: F1
# Phase: Final Round (system-aware)

import numpy as np

def generate_guide_matrix(distance_matrix: np.ndarray) -> np.ndarray:
    n = distance_matrix.shape[0]
    guide_matrix = np.zeros_like(distance_matrix)
    for i in range(n):
        nearby_distances = distance_matrix[i][distance_matrix[i] < np.inf]
        if len(nearby_distances) > 0:
            avg_nearby_distance = np.mean(nearby_distances)
            nearest_penalty = np.min(distance_matrix[i, np.argsort(distance_matrix[i])[:3]])
            for j in range(n):
                if i != j:
                    distance = distance_matrix[i][j]
                    distance_factor = nearest_penalty / (distance + 1e-10)
                    penalty = 1 if distance < avg_nearby_distance else 2
                    guide_matrix[i][j] = distance * (distance_factor + penalty)
    return guide_matrix
