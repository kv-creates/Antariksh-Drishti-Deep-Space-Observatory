# 🚀 Deployment

## Local

```bash
python -m venv .venv && .venv\Scripts\activate
pip install -r requirements.txt
uvicorn src.api:app --port 8000
# open app/index.html
```

## Docker

```bash
docker build -t antariksh .
docker run -p 8000:8000 antariksh
# or
docker compose up --build
```

## Env

Copy `.env.example` → `.env` if you need custom port.

Healthcheck: `GET /health` every 30 s.
