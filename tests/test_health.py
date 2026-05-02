from fastapi.testclient import TestClient
from unittest.mock import patch, AsyncMock
from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_version():
    response = client.get("/version")
    assert response.status_code == 200
    assert "version" in response.json()


def test_db():
    with patch("asyncpg.connect", new_callable=AsyncMock) as mock_connect:
        mock_conn = AsyncMock()
        mock_conn.fetchval.return_value = 1
        mock_connect.return_value = mock_conn

        response = client.get("/db")
        assert response.status_code == 200
        assert response.json() == {"db": "ok", "result": 1}


def test_cache():
    with patch("redis.asyncio.from_url") as mock_from_url:
        mock_client = AsyncMock()
        mock_client.incr.return_value = 1
        mock_from_url.return_value = mock_client

        response = client.get("/cache")
        assert response.status_code == 200
        assert response.json() == {"cache": "ok", "request_count": 1}
