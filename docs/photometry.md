# 🔬 Photometry

![Lightcurve](../docs/images/lightcurve.png)
![SNR](../docs/images/snr-heatmap.png)

## SNR

`snr(F, B=100, RN=5) = F / √(F+B+RN²)` — CCD equation (`src/photometry.py`).

Try the dashboard SNR calculator (`app/index.html#detector`).

## Lightcurve

Box model `lightcurve(t, depth=0.01, period=3.5, dur=0.2)` — scalar or list. Depth → Rp/Rs via `depth_to_radius_ratio = √depth`.

Detection: `src/transit.py:detect(flux, threshold=0.005)` → `{depth, candidate}`.
