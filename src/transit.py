def detect(flux):
    depth=1-min(flux) if flux else 0
    return {'depth':round(depth,4),'candidate':depth>0.005}
