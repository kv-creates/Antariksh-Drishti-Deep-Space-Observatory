import math
MU=398600.4418
def period(a_km):
    return 2*math.pi*math.sqrt(a_km**3/MU)

def propagate(a_km, inc_deg, t_sec):
    import math
    n=math.sqrt(MU/a_km**3)
    x=a_km*math.cos(n*t_sec)
    y=a_km*math.sin(n*t_sec)*math.cos(math.radians(inc_deg))
    z=a_km*math.sin(n*t_sec)*math.sin(math.radians(inc_deg))
    return (x,y,z)
