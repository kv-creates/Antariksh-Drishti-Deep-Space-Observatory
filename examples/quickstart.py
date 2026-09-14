"""Quickstart: 5 lines to first detection."""
from src.orbit import period
from src.photometry import lightcurve
from src.transit import detect

print("period:", round(period(7000), 1))
flux = [lightcurve(t / 10, depth=0.012) for t in range(100)]
print("detection:", detect(flux))
