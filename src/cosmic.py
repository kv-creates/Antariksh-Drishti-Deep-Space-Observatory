"""Cosmic ray helper: inject single-pixel spikes."""
import numpy as np

def add_cosmics(image: np.ndarray, n: int = 5, amp: float = 500.0, seed: int = 1):
    """Add n cosmic hits (deterministic)."""
    rng = np.random.default_rng(seed)
    out = image.copy()
    h, w = out.shape
    for _ in range(n):
        x, y = rng.integers(0, w), rng.integers(0, h)
        out[y, x] += amp
    return out
