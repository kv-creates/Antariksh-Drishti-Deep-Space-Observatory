"""Metrics: recall, efficiency, SNR error."""
from src.transit import detect
from src.scheduler import schedule
from src.photometry import snr

def recall(depths=(0.012,), threshold=0.005) -> float:
    hits = sum(1 for d in depths if detect([1, 1 - d, 1], threshold=threshold)["candidate"])
    return hits / len(depths) if depths else 0.0

def sched_efficiency(sample=None) -> float:
    sample = sample or [{"id": "a", "priority": 1, "duration": 10, "sun": 100}]
    return schedule(sample)["efficiency"]

def snr_error(flux=2000) -> float:
    import math
    expected = flux / math.sqrt(flux + 100 + 25)
    return abs(snr(flux) - expected) / expected
