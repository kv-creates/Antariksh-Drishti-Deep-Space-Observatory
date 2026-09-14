"""End-to-end demo: orbit → schedule → photometry → detection."""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.orbit import period
from src.scheduler import schedule
from src.photometry import lightcurve, snr
from src.transit import detect

def main():
    print("period 7000km:", round(period(7000), 1))
    reqs = [
        {"id": "TOI-715 b", "priority": 9.2, "duration": 60, "sun": 120},
        {"id": "HD 209458 b", "priority": 8.7, "duration": 30, "sun": 40},
        {"id": "K2-18 b", "priority": 8.1, "duration": 45, "sun": 110, "lat": 0, "lon": 0},
    ]
    print("schedule:", schedule(reqs))
    flux = [lightcurve(t, depth=0.012) for t in [i * 0.1 for i in range(100)]]
    print("detect:", detect(flux))
    print("snr(2000):", round(snr(2000), 1))

if __name__ == "__main__":
    main()
