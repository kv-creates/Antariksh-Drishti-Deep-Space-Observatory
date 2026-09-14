"""Physics edge-case coverage."""
import pytest
from src.orbit import period, period_j2, semi_major_from_period
from src.photometry import snr, lightcurve, depth_to_radius_ratio
from src.scheduler import schedule, saa_free
from src.transit import detect

def test_period_range():
    assert 5000 < period(7000) < 7000
    with pytest.raises(ValueError):
        period(6000)

def test_j2_close_to_kepler():
    assert abs(period_j2(7000) - period(7000)) / period(7000) < 0.01

def test_invert():
    assert abs(semi_major_from_period(period(7000)) - 7000) < 1

def test_snr_positive():
    assert snr(2000) > 10

def test_lightcurve_list():
    assert lightcurve([0, 1.75, 5.0], depth=0.012)[-1] < 1

def test_depth_ratio():
    assert abs(depth_to_radius_ratio(0.01) - 0.1) < 1e-9

def test_saa():
    assert saa_free(0, 0) and not saa_free(-10, -40)

def test_schedule_efficiency():
    out = schedule([{"id":"a","priority":1,"duration":10,"sun":100}])
    assert out["efficiency"] == 1.0
    assert detect([1, 0.988, 1])["candidate"]
