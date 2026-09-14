# 🛠️ Operations

Nightly flow:

```bash
python scripts/check_data.py   # CSV sanity
python scripts/generate_visuals.py  # refresh docs/images
pytest -q                      # 15+ tests green
python scripts/run_demo.py     # end-to-end demo
uvicorn src.api:app --port 8000  # serve
```

SAA blackouts + Sun >85° enforced in scheduler. Alt >15° + Moon >20° in `src/visibility.py:visible`.
