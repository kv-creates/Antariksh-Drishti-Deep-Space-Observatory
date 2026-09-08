from fastapi import FastAPI
from .orbit import period
from .transit import detect
app=FastAPI(title='Antariksh-Drishti')
@app.get('/health')
def h(): return {'status':'ok'}
@app.get('/period/{a}')
def p(a: float): return {'period_s':period(a)}
@app.post('/detect')
def d(body: dict): return detect(body.get('flux',[]))
