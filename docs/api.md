# 🔌 API

Base: `uvicorn src.api:app --reload --port 8000` → http://127.0.0.1:8000/docs

| Method | Path | Body | Returns |
|--------|------|------|---------|
| GET | `/health` | — | `{status, service, version}` |
| GET | `/period/{a}` | — | `{radius_km, period_s, period_min}` 422 if out of range |
| POST | `/detect` | `{flux:[...], threshold?}` | `{depth, candidate}` |
| POST | `/detect-legacy` | `{flux:[...]}` | `{depth, candidate}` |
| POST | `/schedule` | `{requests:[{id,priority,duration,sun,lat,lon}]}` | `{scheduled, timeline, efficiency}` |
| GET | `/snr/{flux}?background=&read_noise=` | — | `{flux, snr}` |

Curl:

```bash
curl localhost:8000/health
curl localhost:8000/period/7000
curl localhost:8000/snr/2000
curl -X POST localhost:8000/detect -H "Content-Type: application/json" -d '{"flux":[1,0.988,1]}'
curl -X POST localhost:8000/schedule -H "Content-Type: application/json" -d '{"requests":[{"id":"a","priority":5,"duration":10,"sun":120}]}'
```
