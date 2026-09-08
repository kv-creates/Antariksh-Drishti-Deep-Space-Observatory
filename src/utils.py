import math
def sep(ra1,dec1,ra2,dec2):
    return math.degrees(math.acos(max(-1,min(1,math.sin(math.radians(dec1))*math.sin(math.radians(dec2))+math.cos(math.radians(dec1))*math.cos(math.radians(dec2))*math.cos(math.radians(ra1-ra2))))))
