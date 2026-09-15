import math
from src.orbit import period, semi_major_from_period, propagate

def test_period_monotone():
    assert period(7000) < period(8000) < period(10000)

def test_invert_roundtrip():
    for a in [6600, 7000, 8000, 42164]:
        assert abs(semi_major_from_period(period(a)) - a) < 1e-6

def test_propagate_radius():
    for t in [0, 1000, 5000]:
        x,y,z = propagate(7000, 51.6, t)
        r = math.sqrt(x*x+y*y+z*z)
        assert abs(r-7000) < 1e-6
