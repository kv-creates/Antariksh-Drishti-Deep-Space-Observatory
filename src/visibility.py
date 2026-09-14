"""Visibility: Sun + Moon + altitude gates."""

def visible(sun_angle: float, moon_sep: float, alt_deg: float = 30.0) -> bool:
    """Visible if Sun>85°, Moon sep>20°, alt>15° (alt optional for back-compat)."""
    return bool(sun_angle > 85 and moon_sep > 20 and alt_deg > 15)

def sun_ok(sun_angle: float) -> bool:
    return sun_angle > 85
