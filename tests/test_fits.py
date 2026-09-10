from src.fits_header import header
def test_h():
    assert header()['TELESCOP']=='Antariksh-1'
