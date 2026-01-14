from fastapi import FastAPI
from app.version import VERSION
import os

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/version")
def version():
    return {"version": os.getenv("APP_VERSION", VERSION)}
