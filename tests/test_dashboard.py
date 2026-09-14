"""Dashboard + API contract tests (no server needed)."""
import os

def test_dashboard_exists():
    assert os.path.exists("app/index.html")
    html = open("app/index.html", encoding="utf-8").read()
    for anchor in ["#orbits", "#transits", "#schedule", "#detector", "app.js", "styles.css"]:
        assert anchor in html

def test_images_committed():
    for img in ["hero-orbits.png","lightcurve.png","hr-diagram.png","schedule-gantt.png","snr-heatmap.png","pipeline.png"]:
        assert os.path.exists(f"docs/images/{img}")

def test_api_contract():
    from src.api import app
    routes = {r.path for r in app.routes}
    assert "/health" in routes and "/detect" in routes
