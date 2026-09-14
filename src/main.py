"""CLI demo: period + transit detection."""
from .orbit import period
from .transit import detect

def demo():
    print("Antariksh-Drishti v1.3.0")
    print("period 7000km", round(period(7000), 1), "s")
    print(detect([1, 0.99, 1]))

if __name__ == "__main__":
    demo()
