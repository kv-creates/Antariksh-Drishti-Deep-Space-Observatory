"""Magnitudes: Pogson scale helpers."""
import math

def flux_to_mag(flux: float, zero_point: float = 0.0) -> float:
    """Flux → magnitude: m = -2.5 log10(F) + ZP."""
    return -2.5 * math.log10(max(1e-9, flux)) + zero_point

def mag_to_flux(mag: float, zero_point: float = 0.0) -> float:
    """Magnitude → flux."""
    return 10 ** (-(mag - zero_point) / 2.5)
