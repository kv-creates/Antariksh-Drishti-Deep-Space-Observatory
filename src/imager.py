import numpy as np
def synthetic(stars=50, size=64):
    img=np.random.poisson(10,(size,size)).astype(float)
    for _ in range(stars):
        x,y=np.random.randint(0,size,2)
        img[y,x]+=200
    return img
