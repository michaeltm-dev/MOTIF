import numpy as np

def generate_guide_matrix(distance_matrix: np.ndarray) -> np.ndarray:
    n = distance_matrix.shape[0]
    guide_matrix = np.zeros((n, n))
    criticality = np.sum(distance_matrix, axis=1)
    nearest_neighbors = np.partition(distance_matrix, 2)[:, :3]
    for i in range(n):
        for j in range(n):
            if i != j:
                edge_penalty = distance_matrix[i, j] / (criticality[i] - distance_matrix[i, j] + 1e-6)
                nearest_penalty = (distance_matrix[i, j] / (nearest_neighbors[i][0] + 1e-6)) * 0.7
                guide_matrix[i, j] = edge_penalty + nearest_penalty
    guide_matrix -= np.min(guide_matrix)
    normalized_matrix = guide_matrix / (np.max(guide_matrix) + 1e-8) if np.max(guide_matrix) > 0 else guide_matrix
    return normalized_matrix
