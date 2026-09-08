from src.photometry import snr
def test_snr():
    assert snr(1000)>5
