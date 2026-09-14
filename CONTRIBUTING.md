# 🤝 Contributing to Antariksh-Drishti

Thanks for helping build open space science!

## Quick workflow

1. Fork + `git clone`
2. `python -m venv .venv && pip install -r requirements.txt`
3. Branch: `git checkout -b feat/my-change`
4. Change code + add/extend tests in `tests/`
5. Run `pytest -q` and `python scripts/generate_visuals.py`
6. Commit with [Conventional Commits](https://www.conventionalcommits.org/): `feat:`, `fix:`, `docs:`, `test:`, `chore:`
7. Push + open PR (fill `.github/pull_request_template.md`)

## Standards

- Python 3.11+, type hints + docstrings for new `src/` functions
- Keep back-compat for `period`, `detect`, `schedule`, `snr` signatures
- Regenerate `docs/images/` if visuals logic changed
- Update `CHANGELOG.md` for user-facing changes

## Code of Conduct

Be kind — see `CODE_OF_CONDUCT.md`. Report issues to maintainers.
