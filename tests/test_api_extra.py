from fastapi.testclient import TestClient
from src.api import app
c=TestClient(app)
def test_snr():
    r=c.get("/snr/2000"); assert r.status_code==200 and r.json()["snr"]>0
def test_schedule():
    r=c.post("/schedule", json={"requests":[{"id":"a","priority":1,"duration":10,"sun":100}]})
    assert r.status_code==200 and r.json()["scheduled"]==1
def test_period_validation():
    assert c.get("/period/6000").status_code==422
