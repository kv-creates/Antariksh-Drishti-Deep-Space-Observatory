from src.detrend import median_detrend
def test_d():
    assert len(median_detrend([1,2,3]))==3
