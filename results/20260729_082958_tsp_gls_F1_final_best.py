import numpy as np

def generate_guide_matrix(distance_matrix: np.ndarray) -> np.ndarray:
    n = distance_matrix.shape[0]
    valid_distances = distance_matrix[distance_matrix != 0]
    avg_distance = np.mean(valid_distances)
    variance = np.var(valid_distances)
    nearest_neighbors = np.min(distance_matrix + np.eye(n) * np.max(valid_distances), axis=1)
    weights = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                weights[i, j] = (avg_distance + nearest_neighbors[i] - distance_matrix[i, j] + 0.5 * variance) / (avg_distance + 0.5 * variance)
    guide_matrix = distance_matrix * np.clip(weights, 0.65, 1.75)
    return guide_matrix
