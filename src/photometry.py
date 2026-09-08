import math
def snr(flux, background=100, read_noise=5):
    import math
    return flux/math.sqrt(flux+background+read_noise**2)

def lightcurve(t, depth=0.01, period=3.5, dur=0.2):
    ph=((t+period/2)%period)-period/2
    return 1-depth if abs(ph)<dur/2 else 1.0
