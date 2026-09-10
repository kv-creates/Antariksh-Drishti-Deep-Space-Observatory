from src.coords import altaz
def test_altaz():
    assert altaz(0,0,0,0)['alt']==30.0
