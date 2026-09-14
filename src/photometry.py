"""Photometry: CCD SNR equation and analytic transit lightcurves.

SNR = F / sqrt(F + B + RN^2)
lightcurve(): box-shaped transit, vectorized over scalars or sequences.
"""
import math
from typing import Union, List

def snr(flux: float, background: float = 100, read_noise: float = 5) -> float:
    """Signal-to-noise for aperture flux F (electrons)."""
    if flux < 0 or background < 0 or read_noise < 0:
        raise ValueError("flux/background/read_noise must be non-negative")
    return flux / math.sqrt(flux + background + read_noise ** 2)

def _single(t: float, depth=0.01, period=3.5, dur=0.2) -> float:
    ph = ((t + period / 2) % period) - period / 2
    return 1 - depth if abs(ph) < dur / 2 else 1.0

def lightcurve(t: Union[float, List[float]], depth=0.01, period=3.5, dur=0.2):
    """Box transit model; accepts scalar or list (returns same shape)."""
    if isinstance(t, (list, tuple)):
        return [_single(x, depth, period, dur) for x in t]
    return _single(float(t), depth, period, dur)

def depth_to_radius_ratio(depth: float) -> float:
    """Rp/Rs = sqrt(depth)."""
    if depth < 0 or depth > 1:
        raise ValueError("depth must be in [0,1]")
    return math.sqrt(depth)
