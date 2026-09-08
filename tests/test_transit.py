from src.transit import detect
def test_detect():
    assert detect([1,0.99,1])['candidate']==True
