# Best Round 1 implementation for update_pheromone
# Strategy ID: F3
# Winner: P1
# Best cost: 28.582407
# P1 cost: 28.582407
# P2 cost: 28.640694

import numpy as np

def update_pheromone(
    pheromone: np.ndarray,
    paths: np.ndarray,
    costs: np.ndarray,
    iteration: int,
    n_iterations: int,
) -> np.ndarray:
    pheromone = np.asarray(pheromone, dtype=np.float64).copy()
    paths = np.asarray(paths)
    costs = np.asarray(costs, dtype=np.float64)

    eps = 1e-12
    if pheromone.size == 0 or paths.size == 0 or costs.size == 0:
        return pheromone
    if paths.ndim != 2:
        np.clip(pheromone, eps, 1e6, out=pheromone)
        return pheromone

    n_cities, n_ants = paths.shape
    if n_cities < 2 or n_ants < 1:
        np.clip(pheromone, eps, 1e6, out=pheromone)
        return pheromone

    finite = np.isfinite(costs) & (costs > eps)
    if not np.any(finite):
        np.clip(pheromone, eps, 1e6, out=pheromone)
        return pheromone

    valid_idx = np.flatnonzero(finite)
    valid_costs = costs[valid_idx]
    order = valid_idx[np.argsort(valid_costs)]

    mean_cost = float(np.mean(valid_costs))
    med_cost = float(np.median(valid_costs))
    if not np.isfinite(mean_cost) or mean_cost <= eps:
        mean_cost = float(np.min(valid_costs))
    if not np.isfinite(med_cost) or med_cost <= eps:
        med_cost = mean_cost

    progress = 0.0 if n_iterations <= 1 else float(np.clip(iteration / max(1, n_iterations - 1), 0.0, 1.0))

    evap = 0.94 - 0.16 * progress
    evap = float(np.clip(evap, 0.74, 0.95))
    pheromone *= evap

    elite_k = max(1, min(order.size, int(np.ceil((0.16 + 0.14 * (1.0 - progress)) * n_ants))))
    rank_w = 1.0 / (np.arange(elite_k, dtype=np.float64) + 1.0)
    rank_w /= np.sum(rank_w)

    quality_ref = 0.5 * (mean_cost + med_cost)
    base = (0.82 + 0.70 * progress) / max(1, n_cities)

    edge_hits = np.zeros_like(pheromone)
    edge_sum = np.zeros_like(pheromone)

    def add_tour(tour, amount, collect=False):
        if not np.isfinite(amount) or amount <= 0:
            return
        tour = np.asarray(tour, dtype=np.int64)
        for i in range(n_cities):
            a = int(tour[i])
            b = int(tour[(i + 1) % n_cities])
            if 0 <= a < pheromone.shape[0] and 0 <= b < pheromone.shape[1]:
                pheromone[a, b] += amount
                pheromone[b, a] += amount
                if collect:
                    edge_hits[a, b] += 1.0
                    edge_hits[b, a] += 1.0
                    edge_sum[a, b] += amount
                    edge_sum[b, a] += amount

    for w, idx in zip(rank_w, order[:elite_k]):
        c = float(costs[idx])
        if np.isfinite(c) and c > eps:
            amt = base * w * (quality_ref / (c + eps))
            add_tour(paths[:, idx], amt, collect=True)

    best_idx = int(order[0])
    best_cost = float(costs[best_idx])
    if np.isfinite(best_cost) and best_cost > eps:
        best_amt = base * (3.0 + 1.1 * progress) * (quality_ref / (best_cost + eps))
        add_tour(paths[:, best_idx], best_amt, collect=True)

    if elite_k >= 2:
        second_idx = int(order[1])
        second_cost = float(costs[second_idx])
        if np.isfinite(second_cost) and second_cost > eps:
            add_tour(paths[:, second_idx], base * (1.05 + 0.75 * (1.0 - progress)) * (mean_cost / (second_cost + eps)))

    if elite_k >= 3:
        consensus = edge_sum / np.maximum(edge_hits, 1.0)
        consensus *= (edge_hits >= 2)
        pheromone += (0.11 + 0.11 * (1.0 - progress)) * consensus

    if n_cities > 3:
        tour = np.asarray(paths[:, best_idx], dtype=np.int64)
        smooth_amt = (0.16 + 0.26 * (1.0 - progress)) * base * (mean_cost / (best_cost + eps))
        for i in range(n_cities):
            a = int(tour[i])
            b = int(tour[(i + 2) % n_cities])
            if 0 <= a < pheromone.shape[0] and 0 <= b < pheromone.shape[1]:
                pheromone[a, b] += 0.18 * smooth_amt
                pheromone[b, a] += 0.18 * smooth_amt

    if pheromone.shape[0] == pheromone.shape[1]:
        d = np.diag_indices_from(pheromone)
        pheromone[d] *= 0.5

    np.clip(pheromone, eps, 1e6, out=pheromone)
    return pheromone
