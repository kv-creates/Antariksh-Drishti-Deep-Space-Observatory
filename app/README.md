# 🖥️ Antariksh-Drishti Dashboard

Zero-build mission dashboard — just open `index.html` in a browser. No npm, no bundler.

## Open

```bash
# option 1: double-click app/index.html
# option 2: serve locally
python -m http.server 8080 --directory app
# → http://localhost:8080/
```

## What is inside

| File | Purpose |
|------|---------|
| `index.html` | Semantic sections: mission, orbits, transits, targets, schedule, detector, pipeline |
| `styles.css` | Antariksh dark-space design system (CSS variables, responsive, print) |
| `app.js` | Canvas renders: orbit preview, lightcurve sketch, SNR bar + mission clock |

## Images

All PNGs are committed renders from `../docs/images/` (via `../scripts/generate_visuals.py`):

- `hero-orbits.png` — constellation
- `lightcurve.png` — 1.2% transit
- `hr-diagram.png` — 300 targets
- `schedule-gantt.png` — JWST-like queue
- `snr-heatmap.png` — detector
- `pipeline.png` — architecture

## Accessibility

- Skip link, semantic landmarks, `aria-label` on nav/canvas
- Keyboard-focusable canvases (`tabindex=0`)
- `prefers-reduced-motion` disables pulse animation
- Print stylesheet hides nav/CTA for clean reports

## Browser support

Evergreen Chrome / Edge / Firefox / Safari. No external fonts or CDN required (shields in hero degrade gracefully offline).
