from fastapi.testclient import TestClient

from little_syntax.api import app


client = TestClient(app)


def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_run_code_endpoint():
    response = client.post(
        "/run",
        json={"source": 'say "Hello, traveler!"'},
    )

    assert response.status_code == 200
    body = response.json()

    assert body["output"] == ["Hello, traveler!"]
    assert body["errors"] == []
    assert body["variables"] == {}


def test_run_code_endpoint_returns_errors():
    response = client.post(
        "/run",
        json={"source": "say name"},
    )

    assert response.status_code == 200
    body = response.json()

    assert body["output"] == []
    assert "I don't know what 'name' means yet" in body["errors"][0]
