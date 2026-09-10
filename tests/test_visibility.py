from src.visibility import visible
def test_vis():
    assert visible(100,30)==True
    assert visible(10,30)==False
