# Final Round optimized implementation for compute_probabilities
# Strategy ID: F2
# Phase: Final Round (system-aware)

import numpy as np

def compute_probabilities(
    pheromone: np.ndarray,
    heuristic: np.ndarray,
    iteration: int,
    n_iterations: int
) -> np.ndarray:
    p = np.asarray(pheromone, dtype=np.float64)
    h = np.asarray(heuristic, dtype=np.float64)

    if p.size == 0:
        return p.astype(np.float64, copy=False)

    eps = 1e-12
    p = np.where(np.isfinite(p), p, 0.0)
    h = np.where(np.isfinite(h), h, 0.0)

    if n_iterations <= 1:
        t = 1.0
    else:
        t = np.clip(iteration / (n_iterations - 1), 0.0, 1.0)

    tau = t * t * (3.0 - 2.0 * t)

    p = np.maximum(p, eps)
    h = np.maximum(h, eps)

    mp = np.median(p[p > 0]) if np.any(p > 0) else 1.0
    mh = np.median(h[h > 0]) if np.any(h > 0) else 1.0
    p = p / max(mp, eps)
    h = h / max(mh, eps)

    lp = np.log(p)
    lh = np.log(h)

    alpha = 0.35 + 2.65 * tau
    beta = 3.20 - 2.30 * tau
    gamma = 0.20 * (1.0 - tau) + 0.05 * tau

    mixed = alpha * lp + beta * lh + gamma * (lp + lh)
    mixed -= np.max(mixed)
    mixed = np.clip(mixed, -60.0, 60.0)

    w = np.exp(mixed)
    w[~np.isfinite(w)] = 0.0
    return w + eps
