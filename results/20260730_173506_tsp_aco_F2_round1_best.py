# Best Round 1 implementation for compute_probabilities
# Strategy ID: F2
# Winner: P2
# Best cost: 28.640336
# P1 cost: 28.745423
# P2 cost: 28.640336

import numpy as np

def compute_probabilities(
    pheromone: np.ndarray,
    heuristic: np.ndarray,
    iteration: int,
    n_iterations: int
) -> np.ndarray:
    eps = 1e-12
    p = np.asarray(pheromone, dtype=np.float64)
    h = np.asarray(heuristic, dtype=np.float64)

    if p.size == 0:
        return p.astype(np.float64)

    p = np.where(np.isfinite(p) & (p > 0.0), p, 0.0)
    h = np.where(np.isfinite(h) & (h > 0.0), h, 0.0)

    if not np.any(p > 0.0):
        p = np.ones_like(p)
    if not np.any(h > 0.0):
        h = np.ones_like(h)

    p_pos = p[p > 0.0]
    h_pos = h[h > 0.0]
    p_lo = np.percentile(p_pos, 25) if p_pos.size else 1.0
    p_hi = np.percentile(p_pos, 75) if p_pos.size else 1.0
    h_lo = np.percentile(h_pos, 25) if h_pos.size else 1.0
    h_hi = np.percentile(h_pos, 75) if h_pos.size else 1.0

    p_scale = 0.5 * (p_lo + p_hi) + eps
    h_scale = 0.5 * (h_lo + h_hi) + eps
    p = p / p_scale
    h = h / h_scale

    t = 0.0 if n_iterations <= 1 else np.clip(iteration / (n_iterations - 1), 0.0, 1.0)
    s = t * t * (3.0 - 2.0 * t)

    alpha = 0.70 + 2.05 * (s ** 1.20)
    beta = 2.75 - 1.55 * (s ** 0.85)

    lp = np.log1p(p)
    lh = np.log1p(h)
    lp = (lp - np.mean(lp)) / (np.std(lp) + eps)
    lh = (lh - np.mean(lh)) / (np.std(lh) + eps)

    mix = alpha * lp + beta * lh
    mix += 0.12 * np.tanh(lp * lh)
    mix += 0.05 * (lp - lh)
    mix = np.clip(mix, -60.0, 60.0)

    w = np.exp(mix)
    w = np.where(np.isfinite(w) & (w > 0.0), w, 0.0)
    return w
