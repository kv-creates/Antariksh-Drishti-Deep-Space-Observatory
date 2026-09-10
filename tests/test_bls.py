from src.bls import bls_power
def test_bls():
    assert bls_power([],3.5)>bls_power([],10)
