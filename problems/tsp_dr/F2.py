import numpy as np

def city_badness(tour_idx: int, tour: list[int], distances: np.ndarray) -> float:
    n = len(tour)
    
    city = tour[tour_idx]
    prev_city = tour[(tour_idx - 1) % n]
    next_city = tour[(tour_idx + 1) % n]
    
    # Badness = sum of distances to neighbors
    # Cities with long connections are "bad"
    return distances[prev_city, city] + distances[city, next_city]