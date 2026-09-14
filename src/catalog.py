"""Target catalog I/O."""
import csv
from typing import List, Dict

def load(path: str = "data/targets.csv") -> List[Dict]:
    """Load CSV catalog as list of dicts (keys from header)."""
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def filter_bright(rows, mag_key: str = "mag", limit: float = 12.0):
    """Filter rows brighter than limit (missing/invalid mags excluded)."""
    out = []
    for r in rows:
        try:
            if float(r.get(mag_key, 99)) <= limit:
                out.append(r)
        except (TypeError, ValueError):
            continue
    return out
