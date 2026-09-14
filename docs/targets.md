# 🎯 Targets

![HR](../docs/images/hr-diagram.png)

300-star sample (`data/targets.csv`): Teff, logL, mag, priority.

- **G/K dwarfs (62%)** — high priority, deep transits, low noise
- **M dwarfs (22%)** — medium, small stars boost depth
- **Giants (16%)** — low, diluted depths

Load with `src/catalog.py:load`, filter with `filter_bright(limit=12)`.
