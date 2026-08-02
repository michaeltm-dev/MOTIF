import numpy as np

def generate_guide_matrix(distance_matrix: np.ndarray) -> np.ndarray:
    n = distance_matrix.shape[0]
    guide_matrix = np.zeros_like(distance_matrix)
    total_distances = np.sum(distance_matrix, axis=1)
    neighbor_weights = np.sum(distance_matrix < np.inf, axis=1)
    for i in range(n):
        for j in range(n):
            if i != j and distance_matrix[i, j] < np.inf:
                relative_distance = distance_matrix[i, j] / total_distances[i]
                criticality = 1 / (neighbor_weights[j] + 1)
                penalty = (1 + relative_distance) ** 2 * criticality
                guide_matrix[i, j] = distance_matrix[i, j] * penalty
    return guide_matrix / np.max(guide_matrix)
