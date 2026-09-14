"""FITS header stub (no astropy dependency)."""

def header(target: str = "HD209458", observer: str = "Antariksh-1") -> dict:
    """Minimal FITS-like header dict."""
    return {
        "OBJECT": target,
        "TELESCOP": observer,
        "INSTRUME": "AD-CMOS-1K",
        "BUNIT": "electron",
        "CREATOR": "antariksh-drishti v1.3.0",
    }
