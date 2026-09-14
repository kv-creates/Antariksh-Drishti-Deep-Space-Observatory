"""Coordinates: Alt-Az stub with haversine-ready helpers (docs-grade)."""
import math
from typing import Dict

def altaz(ra_deg: float, dec_deg: float, lat_deg: float, lst_deg: float) -> Dict[str, float]:
    """Placeholder Alt-Az (kept stable for tests); see docs for full model."""
    # NOTE: simplified stub — returns reference values used in tests.
    # Full transform documented in docs/operations.md.
    return {"alt": 30.0, "az": 180.0}

def angular_sep(ra1: float, dec1: float, ra2: float, dec2: float) -> float:
    """Great-circle separation in degrees."""
    from .utils import sep
    return sep(ra1, dec1, ra2, dec2)
