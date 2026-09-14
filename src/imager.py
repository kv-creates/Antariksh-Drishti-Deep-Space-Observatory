"""Synthetic star-field imager: Poisson sky + Gaussian PSF stars.

Deterministic when seed is given — required for reproducible docs/images.
"""
import numpy as np

def _add_star(img, x, y, flux, sigma=1.0):
    s = int(3 * sigma)
    h, w = img.shape
    for dy in range(-s, s + 1):
        for dx in range(-s, s + 1):
            xx, yy = x + dx, y + dy
            if 0 <= xx < w and 0 <= yy < h:
                psf = flux * np.exp(-(dx ** 2 + dy ** 2) / (2 * sigma ** 2))
                img[yy, xx] += psf

def synthetic(stars: int = 50, size: int = 64, seed: int = 0, sky: float = 10.0):
    """Generate synthetic image (size x size)."""
    rng = np.random.default_rng(seed)
    img = rng.poisson(sky, (size, size)).astype(float)
    for _ in range(stars):
        x, y = rng.integers(0, size, 2)
        _add_star(img, int(x), int(y), flux=200.0)
    return img

def add_transit_dimming(img, factor: float = 0.99):
    """Scale image to emulate transit dimming (for demos)."""
    return img * factor
