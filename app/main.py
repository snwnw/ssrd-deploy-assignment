from fastapi import FastAPI
from app.version import VERSION
import os
import asyncpg
import redis.asyncio as redis

app = FastAPI()

DATABASE_URL = os.getenv("DATABASE_URL")
REDIS_URL = os.getenv("REDIS_URL","redis://redis:6379")


@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/version")
def version():
    return {"version": os.getenv("APP_VERSION", VERSION)}

@app.get("/db")
async def db_check():
    conn = await asyncpg.connect(DATABASE_URL)
    result = await conn.fetchval("SELECT 1")
    await conn.close()
    return {"db": "ok", "result": result}

@app.get("/cache")
async def cache_check():
    client = redis.from_url(REDIS_URL)
    count = await client.incr("request_count")
    await client.aclose()
    return {"cache": "ok", "request_count": count}
