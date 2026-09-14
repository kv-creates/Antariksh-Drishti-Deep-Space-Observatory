# Changelog

## v1.3.0 — 2026-09-14 — Professional Dashboard Release

### Added
- Full `app/` dashboard: dark NASA theme, orbit/lightcurve/SNR interactives, responsive + a11y
- Hardened FastAPI (`/health`, `/period/{a}`, `/detect` with validation + CORS)
- PSF imager, vectorized photometry, configurable transit threshold
- Expanded docs: science, ops, API, FAQ, glossary, roadmap
- Legal + meta: Code of Conduct, Security, Citation, PR template, hardened CI/Docker

### Changed
- README: hero, TOC, results gallery, quickstart, performance tables
- All `src/` modules: type hints, docstrings, validation (back-compat kept)
- Requirements pinned; VERSION v1.3.0

### Tests
- 15 legacy + 10 new (dashboard, physics edge cases) — `pytest -q` green

## v1.2.0
- Catalog, BLS stub, calibration, FITS header

## v1.1.0
- Release notes, seeing/airmass

## v1.0.0
- Initial observatory simulator: orbit, scheduler, photometry, transit + 6 visuals
