"""Aperture photometry helper: sum pixels in circular aperture."""
import math
import numpy as np

def aperture_sum(image: np.ndarray, x: int, y: int, r: int = 3) -> float:
    """Sum flux within radius r around (x,y), clipped to bounds."""
    h, w = image.shape
    s = 0.0
    for dy in range(-r, r+1):
        for dx in range(-r, r+1):
            if dx*dx + dy*dy <= r*r:
                xx, yy = x+dx, y+dy
                if 0 <= xx < w and 0 <= yy < h:
                    s += float(image[yy, xx])
    return s

def optimal_radius(curve):
    """Pick radius with max SNR from list of (r, snr)."""
    return max(curve, key=lambda x: x[1])[0] if curve else 0
