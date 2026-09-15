"""Ground track: ECI → lat/lon (spherical Earth, demo)."""
import math
from .orbit import propagate

def eci_to_latlon(x, y, z):
    r = math.sqrt(x*x + y*y + z*z)
    lat = math.degrees(math.asin(z / r)) if r else 0.0
    lon = math.degrees(math.atan2(y, x))
    return lat, ((lon + 180) % 360) - 180

def ground_track(a_km: float, inc_deg: float, t_sec: float):
    x, y, z = propagate(a_km, inc_deg, t_sec)
    return eci_to_latlon(x, y, z)
