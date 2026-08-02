# Best Round 1 implementation for compute_probabilities
# Strategy ID: F2
# Winner: P2
# Best cost: 28.756175
# P1 cost: 28.845628
# P2 cost: 28.756175

import numpy as np

def compute_probabilities(
    pheromone: np.ndarray,
    heuristic: np.ndarray,
    iteration: int,
    n_iterations: int
) -> np.ndarray:
    p = np.asarray(pheromone, dtype=np.float64)
    h = np.asarray(heuristic, dtype=np.float64)

    eps = 1e-12
    p = np.clip(p, eps, None)
    h = np.clip(h, eps, None)

    if n_iterations <= 1:
        t = 1.0
    else:
        t = np.clip(iteration / (n_iterations - 1), 0.0, 1.0)

    s = t * t * (3.0 - 2.0 * t)

    lp = np.log(p)
    lh = np.log(h)

    lp = lp - np.mean(lp)
    lh = lh - np.mean(lh)

    sp = np.std(lp)
    sh = np.std(lh)
    denom = sp + sh + eps
    p_share = sp / denom
    h_share = sh / denom

    if p.size > 1:
        iq_p = np.percentile(lp, 75.0) - np.percentile(lp, 25.0)
        iq_h = np.percentile(lh, 75.0) - np.percentile(lh, 25.0)
        q = 1.0 / (1.0 + np.exp(-(iq_p - iq_h) / (abs(iq_p) + abs(iq_h) + eps)))
    else:
        q = 0.5

    entropy_p = -np.sum(np.exp(lp - np.max(lp)) * (lp - np.max(lp))) / (p.size + eps)
    entropy_h = -np.sum(np.exp(lh - np.max(lh)) * (lh - np.max(lh))) / (h.size + eps)
    ent_bias = 1.0 / (1.0 + np.exp(-(entropy_h - entropy_p)))

    alpha = (0.70 + 1.85 * s) * (0.86 + 0.30 * (1.0 - h_share))
    beta = (2.45 - 1.25 * s) * (0.86 + 0.30 * (1.0 - p_share))

    alpha *= 0.92 + 0.18 * q + 0.10 * ent_bias
    beta *= 1.08 - 0.18 * q + 0.10 * (1.0 - ent_bias)

    sharp = 1.0 + 0.35 * s
    log_w = sharp * (alpha * lp + beta * lh)
    log_w -= np.max(log_w)

    w = np.exp(log_w)
    w = np.where(np.isfinite(w), w, 0.0)
    return w + eps
