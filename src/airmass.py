import math
def airmass(alt_deg):
    import math
    return round(1/max(0.1,math.sin(math.radians(max(5,alt_deg)))),2)
