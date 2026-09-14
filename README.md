<div align="center">

# 🛰️ Antariksh-Drishti — Deep Space Observatory

**End-to-end space-science observatory simulator: orbit design · scheduling · synthetic imaging · photometry · exoplanet detection**

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue.svg)](requirements.txt)
[![CI](https://github.com/kv-creates/Antariksh-Drishti-Deep-Space-Observatory/actions/workflows/ci.yml/badge.svg)](https://github.com/kv-creates/Antariksh-Drishti-Deep-Space-Observatory/actions/workflows/ci.yml)
[![Space Science](https://img.shields.io/badge/space--science-NASA--level-red.svg)](#science-goals)
[![Docs](https://img.shields.io/badge/docs-available-brightgreen.svg)](docs/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-orange.svg)](CONTRIBUTING.md)

*Antariksh (अंतरिक्ष) = Sanskrit for “space”. Drishti (दृष्टि) = “vision”. Together: Vision of Space.*

[🚀 Quick Start](#-quick-start) · [📊 Results](#-results) · [🛰️ Mission](#-mission-overview) · [📖 Docs](docs/) · [🖥️ Live Dashboard](app/index.html) · [🔭 API](#-api-reference)

</div>

---

## 📑 Table of Contents

- [Mission Overview](#-mission-overview)
- [Mission in One Image](#-mission-in-one-image)
- [What This Solves](#-what-this-solves)
- [Results](#-results)
- [Repository Map](#-repository-map)
- [Quick Start](#-quick-start)
- [API Reference](#-api-reference)
- [Reproduce Visuals](#-reproduce-visuals)
- [Performance](#-performance)
- [Roadmap](#️-roadmap)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🛰️ Mission Overview

Low-cost observatories waste **~30% of orbits** on Sun-constraint violations and South Atlantic Anomaly (SAA) passes.
**Antariksh-Drishti** jointly optimizes **orbit → schedule → detection threshold**, with every trade-off visualized and tested.

> All figures below are **generated from code** (`scripts/generate_visuals.py`) and committed under `docs/images/` — no mockups.

<div align="center">

![Hero orbits](docs/images/hero-orbits.png)

***Figure 1 — LEO (7000 km) and MEO constellation orbits** propagated with a J2-aware circular model in `src/orbit.py`. Dark background is intentional for star-field readability.*

</div>

