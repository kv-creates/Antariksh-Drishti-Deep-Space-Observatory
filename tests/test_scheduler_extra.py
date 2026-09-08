from src.scheduler import schedule
def test_sun():
    r=schedule([{'id':'x','priority':1,'duration':5,'sun':10}])
    assert r['scheduled']==0
