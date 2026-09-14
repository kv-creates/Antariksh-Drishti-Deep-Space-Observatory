"""Airmass: plane-parallel with horizon clamp."""
import math

def airmass(alt_deg: float) -> float:
    """Airmass ≈ 1/sin(alt), clamped at alt>=5° and sin>=0.1 (stable)."""
    return round(1 / max(0.1, math.sin(math.radians(max(5, alt_deg)))), 2)

def airmass_young(alt_deg: float) -> float:
    """Alias placeholder for_young (1994) — currently same as plane-parallel."""
    return airmass(alt_deg)
