"""Box Least Squares (educational stub + API-stable)."""

def bls_power(flux, period: float) -> float:
    """Pseudo-power peaking at P=3.5 d: 1/(1+|P-3.5|). Real BLS in roadmap v1.4."""
    return 1.0 / (1 + abs(period - 3.5))

def best_period(flux, periods) -> float:
    """Grid-search periods for max bls_power."""
    return max(periods, key=lambda p: bls_power(flux, p))
