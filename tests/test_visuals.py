import os
def test_visuals_generated():
    for f in ["hero-orbits.png","lightcurve.png","hr-diagram.png","schedule-gantt.png","snr-heatmap.png","pipeline.png"]:
        p=f"docs/images/{f}"
        assert os.path.exists(p), p
        assert os.path.getsize(p) > 1000, p+" too small"
