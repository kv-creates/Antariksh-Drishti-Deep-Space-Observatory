from .orbit import period
from .transit import detect
def demo():
    print('period 7000km', period(7000))
    print(detect([1,0.99,1]))
if __name__=='__main__': demo()
