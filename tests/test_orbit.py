from src.orbit import period
def test_period():
    assert 5000 < period(7000) < 7000
