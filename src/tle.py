"""TLE parsing helpers (minimal, dependency-free)."""
from typing import Dict

def parse_line1(line: str) -> Dict:
    """Parse TLE line 1 for inclination/ecc style demo stub."""
    parts = line.strip().split()
    return {"raw": line.strip(), "tokens": parts}

def parse_tle(l1: str, l2: str) -> Dict:
    """Combine two lines into dict (stub for future SGP4)."""
    return {"line1": parse_line1(l1), "line2": l2.strip(), "valid": len(l1) > 10 and len(l2) > 10}
