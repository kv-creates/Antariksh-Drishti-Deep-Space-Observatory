"""Scheduling example: Sun + SAA filtering."""
from src.scheduler import schedule

requests = [
    {"id": "TOI-715 b", "priority": 9.2, "duration": 60, "sun": 120, "lat": 20, "lon": 30},
    {"id": "SAA-victim", "priority": 9.9, "duration": 30, "sun": 120, "lat": -10, "lon": -40},
    {"id": "Sun-violation", "priority": 9.5, "duration": 30, "sun": 40},
]
result = schedule(requests)
print(f"scheduled {result['scheduled']}/{len(requests)} eff={result['efficiency']}")
for row in result["timeline"]:
    print(row)
