"""Shared math utils."""
import math

def sep(ra1: float, dec1: float, ra2: float, dec2: float) -> float:
    """Angular separation in degrees (haversine-safe)."""
    s = (math.sin(math.radians(dec1)) * math.sin(math.radians(dec2))
         + math.cos(math.radians(dec1)) * math.cos(math.radians(dec2))
         * math.cos(math.radians(ra1 - ra2)))
    return math.degrees(math.acos(max(-1, min(1, s))))

def clamp(x: float, lo: float, hi: float) -> float:
    return max(lo, min(hi, x))
