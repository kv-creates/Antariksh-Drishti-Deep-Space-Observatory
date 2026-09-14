# 🔬 Science Goals

## Primary

1. **Exoplanet transits > 0.5%** — Hot Jupiters around FGK dwarfs. Depth = (Rp/Rs)². Pipeline: `src/photometry.py:lightcurve` → `src/transit.py:detect` → `src/bls.py:best_period`.
2. **Supernova cadence 2 days** — Revisit fields every 48 h; scheduler efficiency ≥ 70%.
3. **NEO astrometry 0.3″** — Synthetic PSF centroiding via `src/imager.py`.

## Success criteria

| Goal | Metric | Threshold |
|------|--------|-----------|
| Transit recall | synthetic 1.2% dips | ≥ 95% at 0.5% thresh |
| Schedule efficiency | scheduled/requested | ≥ 0.70 |
| SNR model | vs CCD equation | ±5% |

See `evaluation/metrics.py` for automated checks.
