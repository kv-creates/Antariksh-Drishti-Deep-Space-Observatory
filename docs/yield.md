# 🪐 Exoplanet Yield Model

Simple estimate: `yield = N_targets × f_transit × recall`

- `N_targets = 300` (`data/targets.csv`)
- `f_transit ≈ 0.05` (hot Jupiters around FGK)
- `recall = 0.95` at 0.5% threshold (`src/transit.py`)

→ ~14 candidates per campaign. Validate with `evaluation/report.py`.

Tune threshold vs false positives via dashboard (`app/index.html#transits`).
