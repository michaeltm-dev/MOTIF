# Final Round optimized implementation for update_pheromone
# Strategy ID: F3
# Phase: Final Round (system-aware)

import numpy as np

def update_pheromone(
    pheromone: np.ndarray,
    paths: np.ndarray,
    costs: np.ndarray,
    iteration: int,
    n_iterations: int,
) -> np.ndarray:
    p = np.asarray(pheromone, dtype=np.float64).copy()
    paths = np.asarray(paths)
    costs = np.asarray(costs, dtype=np.float64).reshape(-1)

    if p.size == 0:
        return p
    if paths.size == 0 or costs.size == 0:
        return np.clip(p, 1e-12, 1e6)

    n_cities, n_ants = paths.shape
    m = min(n_ants, costs.size)
    if m <= 0:
        return np.clip(p, 1e-12, 1e6)

    frac = 0.0 if n_iterations <= 1 else float(np.clip(iteration / (n_iterations - 1), 0.0, 1.0))
    valid = np.isfinite(costs[:m]) & (costs[:m] > 1e-12)
    if not np.any(valid):
        np.clip(p, 1e-12, 1e6, out=p)
        return p

    idx = np.flatnonzero(valid)
    vc = costs[:m][valid]
    order = idx[np.argsort(vc, kind="stable")]

    c_best = float(vc.min())
    c_worst = float(vc.max())
    c_mean = float(vc.mean())
    denom = max(c_worst - c_best, 1e-12)

    evap = 0.28 + 0.42 * frac
    p *= (1.0 - float(np.clip(evap, 0.18, 0.72)))

    elite_n = max(1, min(order.size, int(np.ceil(2.0 + 2.0 * (1.0 - frac)))))
    elite = order[:elite_n]

    for rank, ant in enumerate(elite):
        tour = paths[:, ant].astype(np.int64, copy=False)
        if tour.size != n_cities:
            continue
        c = float(costs[ant])
        if not np.isfinite(c) or c <= 1e-12:
            continue
        quality = (c_worst - c) / denom
        rank_boost = 1.0 / (1.0 + rank)
        deposit = (0.4 + 0.6 * quality) * (c_mean / c) * (0.9 + 0.3 * (1.0 - frac)) * rank_boost
        nxt = np.roll(tour, -1)
        mask = (tour >= 0) & (tour < p.shape[0]) & (nxt >= 0) & (nxt < p.shape[1])
        if np.any(mask):
            a = tour[mask]
            b = nxt[mask]
            p[a, b] += deposit
            p[b, a] += deposit

    top2 = order[:min(2, order.size)]
    if top2.size > 0:
        extra = (1.2 + 0.8 * frac) / max(c_best, 1e-12)
        for ant in top2:
            tour = paths[:, ant].astype(np.int64, copy=False)
            if tour.size != n_cities:
                continue
            nxt = np.roll(tour, -1)
            mask = (tour >= 0) & (tour < p.shape[0]) & (nxt >= 0) & (nxt < p.shape[1])
            if np.any(mask):
                a = tour[mask]
                b = nxt[mask]
                p[a, b] += extra
                p[b, a] += extra

    mean_p = float(np.mean(p)) if np.isfinite(p).any() else 1.0
    if np.isfinite(mean_p) and mean_p > 0:
        blend = 0.008 + 0.012 * (1.0 - frac)
        p = (1.0 - blend) * p + blend * mean_p

    np.maximum(p, 1e-12, out=p)
    np.clip(p, 1e-12, 1e6, out=p)
    return p
