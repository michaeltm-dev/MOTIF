# Best Round 1 implementation for initialize
# Strategy ID: F1
# Winner: P2
# Best cost: 28.595391
# P1 cost: 28.686309
# P2 cost: 28.595391

import numpy as np

def initialize(distances: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    d = np.asarray(distances, dtype=np.float64)
    n = d.shape[0]
    if n == 0:
        return d.copy(), d.copy()

    eps = 1e-12
    eye = np.eye(n, dtype=bool)
    finite_mask = np.isfinite(d) & ~eye
    vals = d[finite_mask]
    scale = np.median(vals) if vals.size else 1.0
    if not np.isfinite(scale) or scale <= 0:
        scale = 1.0

    dd = d.copy()
    dd[~np.isfinite(dd)] = scale
    np.fill_diagonal(dd, np.inf)

    x = dd / scale
    inv = 1.0 / np.maximum(x, eps)
    np.fill_diagonal(inv, 0.0)

    if n == 1:
        h = np.zeros((1, 1), dtype=np.float64)
        return h, h.copy()

    k = min(max(2, int(np.sqrt(n))), n - 1)
    order = np.argsort(dd, axis=1)
    knn = np.zeros((n, n), dtype=np.float64)
    for i in range(n):
        knn[i, order[i, :k]] = 1.0
    mutual = ((knn + knn.T) > 1.5).astype(np.float64)
    one_side = ((knn + knn.T) > 0.5).astype(np.float64)

    neigh_count = np.maximum(one_side.sum(axis=1), 1.0)
    node_density = 1.0 / np.sqrt(neigh_count)
    node_density /= (node_density.mean() + eps)
    node_factor = np.sqrt(np.outer(node_density, node_density))

    sorted_d = np.sort(dd, axis=1)
    nn1 = sorted_d[:, 0]
    nn2 = sorted_d[:, 1] if n > 2 else sorted_d[:, 0]
    tightness = (nn2 - nn1) / np.maximum(nn2 + nn1, eps)
    tightness = np.clip(tightness, 0.0, 1.0)
    node_tight = np.sqrt(np.outer(1.0 + tightness, 1.0 + tightness))

    shared = knn @ knn.T
    shared = shared.astype(np.float64)
    shared /= (shared.max() if shared.max() > 0 else 1.0)
    np.fill_diagonal(shared, 0.0)

    support = inv @ one_side
    support = 0.5 * (support + support.T)
    np.fill_diagonal(support, 0.0)
    smax = np.max(support)
    if np.isfinite(smax) and smax > 0:
        support /= smax

    bridge = inv @ mutual
    bridge = 0.5 * (bridge + bridge.T)
    np.fill_diagonal(bridge, 0.0)
    bmax = np.max(bridge)
    if np.isfinite(bmax) and bmax > 0:
        bridge /= bmax

    rank_bonus = 1.0 / (1.0 + np.argsort(order, axis=1).astype(np.float64))
    rank_bonus = 0.5 * (rank_bonus + rank_bonus.T)
    np.fill_diagonal(rank_bonus, 0.0)

    penalty = np.zeros((n, n), dtype=np.float64)
    penalty += 0.35 * (1.0 - mutual)
    penalty += 0.25 * (1.0 - one_side)
    penalty += 0.20 * (1.0 - shared)
    penalty = np.clip(penalty, 0.0, 1.0)

    heuristic = inv
    heuristic *= (0.55 + 0.45 * node_factor)
    heuristic *= (1.0 + 0.55 * support + 0.35 * bridge + 0.20 * shared)
    heuristic *= (1.0 + 0.20 * rank_bonus)
    heuristic *= (1.0 + 0.15 * node_tight)
    heuristic *= (1.0 - 0.40 * penalty)
    heuristic = np.maximum(heuristic, 0.0)
    heuristic = 0.5 * (heuristic + heuristic.T)
    np.fill_diagonal(heuristic, 0.0)

    hmax = np.max(heuristic)
    if not np.isfinite(hmax) or hmax <= 0:
        heuristic = np.ones_like(dd, dtype=np.float64)
        np.fill_diagonal(heuristic, 0.0)
        hmax = 1.0
    heuristic = heuristic / hmax

    pheromone = 0.07 + 0.93 * heuristic
    pheromone = 0.5 * (pheromone + pheromone.T)
    np.fill_diagonal(pheromone, 0.0)
    pheromone = np.where(np.isfinite(pheromone), pheromone, 0.07)
    return heuristic, pheromone
