# Best Round 1 implementation for initialize
# Strategy ID: F1
# Winner: P2
# Best cost: 91.962272
# P1 cost: 92.016138
# P2 cost: 91.962272

import numpy as np

def initialize(distances, demands, coords, capacity):
    num_nodes = len(demands)
    heuristic = np.zeros((num_nodes, num_nodes))
    for i in range(num_nodes):
        for j in range(num_nodes):
            if demands[j] <= capacity:
                distance_adjusted = distances[i][j] + 1e-6
                demand_factor = (capacity - demands[j]) / capacity
                heuristic[i][j] = demand_factor / distance_adjusted  * (1 + np.exp(-0.5 * (demands[j] / capacity)))
    pheromone = np.ones_like(distances)
    return heuristic, pheromone