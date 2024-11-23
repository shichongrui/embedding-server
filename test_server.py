from fastapi.testclient import TestClient
from main import app

def test_server():
    with TestClient(app) as client:
        response = client.post("/embeddings", json={
            "text": ["This is some text", "This is also some text"]
        },
        headers={
            "Content-Type": "application/json"
        })

        assert response.status_code == 200
        assert len(response.json()["embeddings"]) == 2