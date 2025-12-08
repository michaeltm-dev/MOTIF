import numpy as np

def generate_guide_matrix(distance_matrix: np.ndarray) -> np.ndarray:
    """
    Parameters
    ----------
    distance_matrix : np.ndarray, shape (n, n)
        Matrix of pairwise distances between cities.

    Returns
    -------
    np.ndarray, shape (n, n)
        Edge importance matrix where guide[i,j] represents how "bad"
        to include edge (i,j) in the tour. Higher values indicate edges
        that are less favorable to include.
    """
    # Default implementation: use distance as guide
    # Longer edges are more likely to be "bad" choices
    return distance_matrix