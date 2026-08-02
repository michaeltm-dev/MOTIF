import numpy as np

def generate_guide_matrix(distance_matrix: np.ndarray) -> np.ndarray:
    n = distance_matrix.shape[0]
    avg_distance = np.mean(distance_matrix[distance_matrix != 0])
    nearest_neighbors = np.zeros(n)
    for i in range(n):
        nearest_neighbors[i] = np.min(distance_matrix[i][distance_matrix[i] != 0])
    weights = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                weights[i, j] = (avg_distance + nearest_neighbors[i] - distance_matrix[i, j]) / avg_distance
    guide_matrix = distance_matrix * np.clip(weights, 0.5, 2)
    return guide_matrix
