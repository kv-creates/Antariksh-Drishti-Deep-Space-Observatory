# 🛰️ Orbits

![Hero](../docs/images/hero-orbits.png)

## Model

- **period(a)** — `T = 2π√(a³/μ)`, μ = 398600.4418 km³/s². Raises `ValueError` if a ≤ 6378 km.
- **propagate(a, inc, t)** — circular inclined ECI, n = √(μ/a³).
- **period_j2(a, inc=51.6°)** — first-order J2 nodal correction.
- **semi_major_from_period(T)** — inverse Kepler.

## Example

```python
from src.orbit import period, propagate
period(7000)  # ≈ 5828.5 s
propagate(7000, 51.6, 0)  # (7000, 0, 0)
```

Tune altitude in dashboard (`app/index.html` slider) — same equation as `app/app.js`.
