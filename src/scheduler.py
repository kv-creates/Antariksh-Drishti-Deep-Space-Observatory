"""Greedy JWST-like scheduler with Sun and SAA constraints.

Policy:
  - sort by descending priority
  - require sun_angle > 85 deg
  - require SAA-free (lat/lon polygon)
  - 5-min slew between accepted observations
"""
from typing import List, Dict

SLEW_MIN = 5
SUN_MIN_DEG = 85

def saa_free(lat: float, lon: float) -> bool:
    """South Atlantic Anomaly polygon: reject (-30<lat<10 and -60<lon<-20)."""
    return not (-30 < lat < 10 and -60 < lon < -20)

def sun_ok(sun_angle_deg: float, threshold: float = SUN_MIN_DEG) -> bool:
    """Sun-avoidance check."""
    return sun_angle_deg > threshold

def schedule(requests: List[Dict]) -> Dict:
    """Greedy schedule.

    Each request: {id, priority, duration, sun?, lat?, lon?}
    Returns: {scheduled, timeline: [{id, start, end}], efficiency}
    """
    req = sorted(requests, key=lambda x: -x.get("priority", 0))
    tl = []
    t = 0
    for r in req:
        if not sun_ok(r.get("sun", 100)):
            continue
        if "lat" in r and "lon" in r and not saa_free(r["lat"], r["lon"]):
            continue
        dur = int(r.get("duration", 10))
        tl.append({"id": r["id"], "start": t, "end": t + dur})
        t += dur + SLEW_MIN
    eff = len(tl) / len(requests) if requests else 0.0
    return {"scheduled": len(tl), "timeline": tl, "efficiency": round(eff, 3)}
