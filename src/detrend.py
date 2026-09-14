"""Detrending: median-baseline (stable) + running-median helper."""
import statistics
from typing import List

def median_detrend(flux: List[float], w: int = 11) -> List[float]:
    """Subtract global median (window w reserved for future running version)."""
    m = statistics.median(flux)
    return [x - m for x in flux]

def running_median(flux: List[float], w: int = 11) -> List[float]:
    """Running median baseline (edge-padded)."""
    n = len(flux)
    out = []
    h = w // 2
    for i in range(n):
        lo, hi = max(0, i - h), min(n, i + h + 1)
        out.append(statistics.median(flux[lo:hi]))
    return out
