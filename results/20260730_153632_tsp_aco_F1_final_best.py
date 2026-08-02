# Final Round optimized implementation for initialize
# Strategy ID: F1
# Phase: Final Round (system-aware)

import numpy as np

def initialize(distances: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    d = np.asarray(distances, dtype=float)
    eps = 1e-12
    if d.size == 0:
        return d.copy(), d.copy()
    if d.ndim != 2 or d.shape[0] != d.shape[1]:
        raise ValueError("distances must be a square matrix")

    n = d.shape[0]
    dd = d.copy()
    np.fill_diagonal(dd, np.inf)

    finite = dd[np.isfinite(dd)]
    if finite.size == 0:
        h = np.zeros_like(dd)
        p = np.zeros_like(dd)
        return h, p

    q25, q50, q75 = np.percentile(finite, [25.0, 50.0, 75.0])
    mad = np.median(np.abs(finite - q50))
    scale = q50 if q50 > eps else (finite.mean() if finite.mean() > eps else 1.0)
    spread = max(q75 - q25, 1.4826 * mad, eps)

    inv = 1.0 / np.maximum(dd, eps)
    inv[~np.isfinite(inv)] = 0.0
    inv /= max(np.max(inv), eps)

    close = np.exp(-np.clip(dd / (scale + eps), 0.0, 80.0))
    close[~np.isfinite(close)] = 0.0
    close /= max(np.max(close), eps)

    row_min = np.min(dd, axis=1, keepdims=True)
    col_min = np.min(dd, axis=0, keepdims=True)
    row_min = np.where(np.isfinite(row_min), row_min, scale)
    col_min = np.where(np.isfinite(col_min), col_min, scale)
    local = np.sqrt(np.maximum((row_min / (dd + eps)) * (col_min / (dd + eps)), 0.0))
    local[~np.isfinite(local)] = 0.0
    local /= max(np.max(local), eps)

    rank = np.argsort(np.argsort(dd, axis=1), axis=1).astype(float)
    topk = max(2, int(np.sqrt(n) + 1))
    candidate = np.maximum(0.0, (topk - rank) / topk)

    z = (scale - dd) / spread
    sig = 1.0 / (1.0 + np.exp(-np.clip(z, -18.0, 18.0)))

    nn = np.argmin(dd, axis=1)
    mutual = np.zeros_like(dd)
    mutual[np.arange(n), nn] = 1.0
    mutual = np.maximum(mutual, mutual.T * mutual)

    sym = 0.5 * (dd + dd.T)
    sym_finite = sym[np.isfinite(sym)]
    sym_scale = np.median(sym_finite) if sym_finite.size else scale
    sym_close = np.exp(-np.clip(sym / (sym_scale + eps), 0.0, 80.0))
    sym_close[~np.isfinite(sym_close)] = 0.0
    sym_close /= max(np.max(sym_close), eps)

    tri = np.maximum(0.0, (row_min + col_min - dd) / (row_min + col_min + eps))
    tri[~np.isfinite(tri)] = 0.0

    core = (
        0.26 * inv +
        0.20 * close +
        0.16 * local +
        0.12 * candidate +
        0.10 * sig +
        0.10 * mutual +
        0.06 * tri
    )
    heuristic = core * (0.82 + 0.18 * sym_close) + 0.05 * local * sym_close
    heuristic = np.where(np.isfinite(heuristic), heuristic, 0.0)
    heuristic = np.maximum(heuristic, 0.0)
    np.fill_diagonal(heuristic, 0.0)
    heuristic = 0.5 * (heuristic + heuristic.T)
    hmax = np.max(heuristic)
    if hmax > 0:
        heuristic /= hmax

    pheromone = (
        1.0 +
        0.28 * close +
        0.16 * local +
        0.10 * candidate +
        0.08 * sig +
        0.14 * mutual +
        0.10 * sym_close +
        0.06 * tri
    )
    pheromone = np.where(np.isfinite(pheromone), pheromone, 1.0)
    pheromone = np.maximum(pheromone, eps)
    np.fill_diagonal(pheromone, 0.0)
    pheromone = 0.5 * (pheromone + pheromone.T)
    pmax = np.max(pheromone)
    if pmax > 0:
        pheromone /= pmax

    return heuristic, pheromone
