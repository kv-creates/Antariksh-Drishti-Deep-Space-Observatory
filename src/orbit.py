"""Orbit mechanics: Kepler periods and J2-aware circular propagation.

References:
  - period(): T = 2*pi*sqrt(a^3 / mu), mu = 398600.4418 km^3/s^2
  - propagate(): circular inclined orbit, mean motion n = sqrt(mu/a^3)
  - period_j2(): first-order J2 secular correction
"""
import math

MU = 398600.4418  # km^3/s^2
EARTH_R_KM = 6378.0
J2 = 1.08263e-3

def period(a_km: float) -> float:
    """Circular Kepler period in seconds.

    Args:
        a_km: semi-major axis / radius in km (must be > Earth radius).

    Raises:
        ValueError: if a_km is non-physical.
    """
    if a_km <= EARTH_R_KM:
        raise ValueError("a_km must exceed Earth radius (6378 km)")
    return 2 * math.pi * math.sqrt(a_km ** 3 / MU)

def propagate(a_km: float, inc_deg: float, t_sec: float):
    """Propagate circular orbit to ECI position (x, y, z) in km."""
    n = math.sqrt(MU / a_km ** 3)
    inc = math.radians(inc_deg)
    x = a_km * math.cos(n * t_sec)
    y = a_km * math.sin(n * t_sec) * math.cos(inc)
    z = a_km * math.sin(n * t_sec) * math.sin(inc)
    return (x, y, z)

def period_j2(a_km: float, inc_deg: float = 51.6) -> float:
    """J2-corrected nodal period (first order)."""
    n0 = (MU / a_km ** 3) ** 0.5
    corr = 1 - 0.75 * J2 * (EARTH_R_KM / a_km) ** 2 * math.cos(math.radians(inc_deg)) ** 2
    return 2 * math.pi / n0 * corr

def semi_major_from_period(t_sec: float) -> float:
    """Invert Kepler's third law: a from period."""
    return (MU * (t_sec / (2 * math.pi)) ** 2) ** (1 / 3)
