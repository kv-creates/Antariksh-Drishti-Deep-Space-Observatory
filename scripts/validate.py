"""Validate physics constants + committed visuals exist."""
import os
from src.orbit import period
assert 5000 < period(7000) < 7000, "period out of range"
for img in ["hero-orbits.png","lightcurve.png","hr-diagram.png","schedule-gantt.png","snr-heatmap.png","pipeline.png"]:
    assert os.path.exists(f"docs/images/{img}"), f"missing {img}"
print("validate: OK")
