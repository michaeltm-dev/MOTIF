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
    ph = np.array(pheromone, dtype=np.float64, copy=True)
    paths = np.asarray(paths)
    costs = np.asarray(costs, dtype=np.float64).reshape(-1)

    if ph.ndim != 2 or ph.shape[0] != ph.shape[1] or paths.ndim != 2:
        return np.nan_to_num(ph, nan=1e-12, posinf=1e6, neginf=1e-12)

    n_cities = ph.shape[0]
    if paths.shape[0] != n_cities or costs.size == 0:
        ph *= 0.95
        np.clip(ph, 1e-12, 1e6, out=ph)
        return np.nan_to_num(ph, nan=1e-12, posinf=1e6, neginf=1e-12)

    valid = np.isfinite(costs) & (costs > 0)
    if not np.any(valid):
        ph *= 0.95
        np.clip(ph, 1e-12, 1e6, out=ph)
        return np.nan_to_num(ph, nan=1e-12, posinf=1e6, neginf=1e-12)

    n_ants = paths.shape[1]
    prog = 0.0 if n_iterations <= 1 else np.clip(iteration / (n_iterations - 1), 0.0, 1.0)

    valid_idx = np.flatnonzero(valid)
    valid_costs = costs[valid]
    order = np.argsort(valid_costs)
    sorted_idx = valid_idx[order]
    best_idx = sorted_idx[0]
    best_cost = max(costs[best_idx], 1e-12)
    med_cost = float(np.median(valid_costs))
    worst_cost = float(np.max(valid_costs))
    spread = max(med_cost - best_cost, 1e-12)
    range_cost = max(worst_cost - best_cost, 1e-12)

    evap = 0.58 - 0.20 * prog
    evap = float(np.clip(evap, 0.36, 0.58))
    ph *= evap

    elite_k = max(1, min(n_ants, int(np.ceil(0.25 * n_ants))))
    elite_idx = sorted_idx[:elite_k]

    def add_tour(tour, weight):
        if weight <= 0 or not np.isfinite(weight):
            return
        tour = np.asarray(tour, dtype=np.int64).ravel()
        if tour.size != n_cities:
            return
        nxt = np.roll(tour, -1)
        np.add.at(ph, (tour, nxt), weight)
        np.add.at(ph, (nxt, tour), weight)

    best_boost = (1.35 + 1.05 * prog) * (1.0 + 0.30 * spread / (best_cost + spread))
    add_tour(paths[:, best_idx], best_boost)

    for r, ant in enumerate(elite_idx):
        c = max(costs[ant], 1e-12)
        rank_w = (elite_k - r) / elite_k
        quality = (best_cost / c) ** 1.45
        quality = np.clip(quality, 0.20, 5.0)
        add_tour(paths[:, ant], 0.80 * rank_w * quality)

    inv = 1.0 / (valid_costs + 1e-12)
    inv /= inv.sum() + 1e-12
    for ant, w in zip(valid_idx, inv):
        c = max(costs[ant], 1e-12)
        local = 1.0 + 0.22 * (range_cost / (c - best_cost + range_cost))
        add_tour(paths[:, ant], 0.14 * w * local * (1.0 - 0.25 * prog))

    ph = 0.5 * (ph + ph.T)
    np.clip(ph, 1e-12, 1e6, out=ph)
    return np.nan_to_num(ph, nan=1e-12, posinf=1e6, neginf=1e-12)
