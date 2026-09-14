"""Transit detection: threshold + BLS-ready helpers."""
from typing import List, Dict

DEFAULT_THRESHOLD = 0.005

def depth(flux: List[float]) -> float:
    """Max depth = 1 - min(flux); 0 for empty."""
    if not flux:
        return 0.0
    return 1 - min(flux)

def detect(flux: List[float], threshold: float = DEFAULT_THRESHOLD) -> Dict:
    """Return {depth, candidate} where candidate = depth > threshold."""
    d = depth(flux)
    return {"depth": round(d, 4), "candidate": bool(d > threshold)}

def snr_depth(depth: float, noise: float) -> float:
    """Depth SNR helper for threshold tuning."""
    if noise <= 0:
        raise ValueError("noise must be positive")
    return depth / noise
