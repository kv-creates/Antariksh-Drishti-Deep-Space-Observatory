"""Micro-benchmark: period + schedule + snr (no external deps)."""
import time
from src.orbit import period
from src.scheduler import schedule
from src.photometry import snr
t0=time.perf_counter()
for _ in range(10000): period(7000)
for _ in range(1000): schedule([{"id":"a","priority":1,"duration":10,"sun":100},{"id":"b","priority":2,"duration":10,"sun":100}])
for _ in range(10000): snr(2000)
print(f"bench: {time.perf_counter()-t0:.3f}s for 21k ops")
