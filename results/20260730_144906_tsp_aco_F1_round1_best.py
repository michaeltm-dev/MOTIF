# Best Round 1 implementation for initialize
# Strategy ID: F1
# Winner: P2
# Best cost: 28.676240
# P1 cost: 28.691357
# P2 cost: 28.676240

import numpy as np

def initialize(distances: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    d = np.asarray(distances, dtype=float)
    if d.size == 0:
        return d.copy(), d.copy()
    if d.ndim != 2 or d.shape[0] != d.shape[1]:
        n = d.shape[0] if d.ndim >= 1 else 0
        z = np.zeros_like(d, dtype=float)
        return z, z

    n = d.shape[0]
    eps = 1e-12
    d = 0.5 * (d + d.T)
    np.fill_diagonal(d, 0.0)

    mask = ~np.eye(n, dtype=bool)
    vals = d[mask]
    finite = vals[np.isfinite(vals) & (vals > 0)]
    if finite.size == 0:
        h = np.ones_like(d, dtype=float)
        p = np.ones_like(d, dtype=float)
        np.fill_diagonal(h, 0.0)
        np.fill_diagonal(p, 0.0)
        return h, p

    scale = np.median(finite)
    if not np.isfinite(scale) or scale <= 0:
        scale = np.mean(finite)
    if not np.isfinite(scale) or scale <= 0:
        scale = 1.0

    inv = np.zeros_like(d, dtype=float)
    np.divide(1.0, d + eps, out=inv, where=d > 0)
    inv[~np.isfinite(inv)] = 0.0
    inv[np.diag_indices(n)] = 0.0

    work = np.where(mask, d, np.inf)
    order = np.argsort(work, axis=1)

    k = max(2, min(n - 1, int(np.sqrt(max(n, 2)))))
    k1 = 1 if n > 1 else 0
    kth_idx = min(k - 1, n - 2) if n > 1 else 0
    nn_idx = 1 if n > 2 else k1

    kth = np.partition(work, kth_idx, axis=1)[:, kth_idx] if n > 1 else np.array([scale])
    nn = np.partition(work, nn_idx, axis=1)[:, nn_idx] if n > 1 else np.array([scale])
    kth = np.where(np.isfinite(kth) & (kth > 0), kth, scale)
    nn = np.where(np.isfinite(nn) & (nn > 0), nn, scale)

    local = np.sqrt(np.outer(kth, kth))
    near = np.sqrt(np.outer(nn, nn))
    local_factor = 1.0 / (1.0 + d / (local + eps))
    near_factor = 1.0 / (1.0 + d / (near + eps))

    ranks = np.full((n, n), np.inf, dtype=float)
    for i in range(n):
        nbrs = order[i]
        nbrs = nbrs[nbrs != i]
        if nbrs.size:
            ranks[i, nbrs] = np.arange(1, nbrs.size + 1, dtype=float)
    mutual = np.minimum(ranks, ranks.T)
    rank_factor = 1.0 / np.log1p(mutual + 1.0)
    rank_factor[~np.isfinite(rank_factor)] = 0.0

    tri = np.zeros((n, n), dtype=float)
    if n > 2:
        top = min(k, n - 1)
        neigh = np.zeros((n, n), dtype=bool)
        for i in range(n):
            neigh[i, order[i, :top]] = True
        support = neigh.astype(int) @ neigh.astype(int).T
        tri = support.astype(float)
        tri = tri / (np.max(tri[mask]) + eps) if np.any(mask) else tri

    # Triangle closure preference: promote edges whose endpoints share good alternatives
    alt = np.zeros((n, n), dtype=float)
    if n > 2:
        top = min(k, n - 1)
        for i in range(n):
            ni = order[i, :top]
            if ni.size == 0:
                continue
            # average closeness to mutual neighborhood
            alt[i] = np.sum(inv[ni], axis=0)
        alt = 0.5 * (alt + alt.T)
        alt = alt / (np.max(alt[mask]) + eps) if np.any(mask) else alt

    finite_d = d[mask]
    q25, q50, q75 = np.percentile(finite_d, [25, 50, 75])
    s1 = max(q50 - q25, eps)
    s2 = max(q75 - q50, eps)
    soft = 1.0 / (1.0 + np.exp((d - q50) / s1))
    soft2 = 1.0 / (1.0 + np.exp((d - q75) / s2))

    node_pref = 1.0 / (0.6 * nn + 0.4 * kth + eps)
    node_pref = node_pref / (np.mean(node_pref) + eps)
    node_factor = np.sqrt(np.outer(node_pref, node_pref))

    heuristic = inv
    heuristic *= (0.30 + 0.70 * near_factor)
    heuristic *= (0.25 + 0.75 * local_factor)
    heuristic *= (0.55 + 0.45 * rank_factor)
    heuristic *= (0.65 + 0.35 * node_factor)
    heuristic *= (0.50 + 0.50 * tri)
    heuristic *= (0.60 + 0.40 * alt)
    heuristic *= (0.45 + 0.35 * soft + 0.20 * soft2)
    heuristic *= 1.0 / (1.0 + 0.10 * (d / (scale + eps)) + 0.02 * (d / (scale + eps)) ** 2)
    heuristic = 0.5 * (heuristic + heuristic.T)
    heuristic[np.diag_indices(n)] = 0.0
    heuristic = np.nan_to_num(heuristic, nan=0.0, posinf=0.0, neginf=0.0)

    hv = heuristic[mask]
    if hv.size == 0:
        pheromone = np.zeros_like(heuristic)
        return heuristic, pheromone

    p20, p50, p80 = np.percentile(hv, [20, 50, 80])
    hmax = np.max(hv)
    if not np.isfinite(hmax) or hmax <= 0:
        hmax = 1.0
    core = 0.45 * (heuristic / (p50 + eps)) + 0.35 * (heuristic / (p80 + eps)) + 0.20 * (heuristic / (p20 + eps))
    pheromone = 0.08 + 0.92 * np.power(np.clip(core, 0.0, None), 1.05)
    pheromone = np.where(heuristic >= p80, pheromone, 0.20 * pheromone + 0.80 * (0.08 + 0.12 * heuristic / (hmax + eps)))
    pheromone = 0.5 * (pheromone + pheromone.T)
    pheromone[np.diag_indices(n)] = 0.0
    pheromone = np.nan_to_num(np.clip(pheromone, 0.0, None), nan=0.08, posinf=1.0, neginf=0.08)

    return heuristic, pheromone
