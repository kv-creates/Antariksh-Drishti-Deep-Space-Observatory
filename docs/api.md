# 🔌 API

Base: `uvicorn src.api:app --reload --port 8000` → `http://127.0.0.1:8000/docs`

| Method | Path | Body | Returns |
|--------|------|------|---------|
| GET | `/health` | — | `{status, service, version}` |
| GET | `/period/{a}` | — | `{radius_km, period_s, period_min}` (422 if out of range) |
| POST | `/detect` | `{flux:[...], threshold?}` | `{depth, candidate}` |
| POST | `/detect-legacy` | `{flux:[...]}` | `{depth, candidate}` |

Example:

```bash
curl localhost:8000/period/7000
curl -X POST localhost:8000/detect -H "Content-Type: application/json" -d '{"flux":[1,0.988,1]}'
```
