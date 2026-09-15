"""Antariksh-Drishti FastAPI service."""
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import List, Dict
from .orbit import period
from .transit import detect
from .scheduler import schedule
from .photometry import snr

app = FastAPI(
    title="Antariksh-Drishti",
    description="Deep Space Observatory: orbit, photometry and transit detection API.",
    version="1.3.0",
    docs_url="/docs",
    redoc_url="/redoc",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

class DetectRequest(BaseModel):
    flux: List[float] = Field(..., min_length=1, description="Normalized flux array")
    threshold: float = Field(0.005, ge=0, le=0.5, description="Depth threshold")

class DetectResponse(BaseModel):
    depth: float
    candidate: bool

class PeriodResponse(BaseModel):
    radius_km: float
    period_s: float
    period_min: float

@app.get("/health", tags=["ops"])
def health():
    """Liveness probe."""
    return {"status": "ok", "service": "antariksh-drishti", "version": "1.3.0"}

@app.get("/period/{a}", response_model=PeriodResponse, tags=["orbit"])
def period_endpoint(a: float):
    """Orbital period for circular radius a (km)."""
    if a < 6500 or a > 50000:
        raise HTTPException(status_code=422, detail="a must be in [6500, 50000] km")
    p = period(a)
    return {"radius_km": a, "period_s": p, "period_min": p / 60.0}

@app.post("/detect", response_model=DetectResponse, tags=["photometry"])
def detect_endpoint(body: DetectRequest):
    """Transit detection from flux series."""
    return detect(body.flux, threshold=body.threshold)

# Back-compat: allow raw dict posts like {"flux": [...]}
@app.post("/detect-legacy", tags=["photometry"])
class ScheduleRequest(BaseModel):
    requests: List[Dict] = Field(..., description="Scheduler requests")

@app.post("/schedule", tags=["scheduler"])
def schedule_endpoint(body: ScheduleRequest):
    return schedule(body.requests)

@app.get("/snr/{flux}", tags=["photometry"])
def snr_endpoint(flux: float, background: float = 100, read_noise: float = 5):
    return {"flux": flux, "snr": snr(flux, background, read_noise)}

def detect_legacy(body: dict):
    return detect(body.get("flux", []))
