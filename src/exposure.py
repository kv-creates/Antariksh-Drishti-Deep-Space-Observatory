"""Exposure-time calculator (CCD equation inversion, demo-grade)."""

def exptime(snr_target: float = 10, flux: float = 1000, overhead_s: float = 0.0) -> float:
    """Required seconds for target SNR at given flux (e-/s)."""
    if flux <= 0:
        raise ValueError("flux must be positive")
    base = round((snr_target ** 2 * 1100) / (flux ** 2) * 100, 2)
    return round(base + overhead_s, 2)

def coadds_needed(snr_target: float, single_snr: float) -> int:
    """N = ceil((target/single)^2)."""
    import math
    if single_snr <= 0:
        raise ValueError("single_snr must be positive")
    return int(math.ceil((snr_target / single_snr) ** 2))
