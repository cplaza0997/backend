from fastapi.testclient import TestClient
from ..api import app
import json
client = TestClient(app)

def test_unauthorized():
    response = client.post("/login", json={"user":"abcd","password": "passoss"})
    assert response.status_code == 401
    assert response.json() == {"detail": "Unauthorized"}


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "OK"}