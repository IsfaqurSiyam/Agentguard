from fastapi.testclient import TestClient


class FakeConnection:
    async def __aenter__(self) -> "FakeConnection":
        return self

    async def __aexit__(self, *args: object) -> None:
        return None

    async def execute(self, *args: object) -> None:
        return None


class FakeEngine:
    def connect(self) -> FakeConnection:
        return FakeConnection()

    async def dispose(self) -> None:
        return None


class FakeRedis:
    async def ping(self) -> bool:
        return True

    async def aclose(self) -> None:
        return None


def test_health_is_available_and_returns_a_correlation_id(client: TestClient) -> None:
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"
    assert response.headers["x-request-id"]


def test_request_id_is_preserved(client: TestClient) -> None:
    response = client.get("/api/v1/health", headers={"X-Request-ID": "test-correlation-id"})
    assert response.headers["x-request-id"] == "test-correlation-id"


def test_ready_checks_backing_services(client: TestClient) -> None:
    client.app.state.db_engine = FakeEngine()
    client.app.state.redis = FakeRedis()
    response = client.get("/api/v1/ready")
    assert response.status_code == 200
    assert response.json()["status"] == "ready"


def test_unknown_path_uses_problem_details(client: TestClient) -> None:
    response = client.get("/api/v1/not-found")
    assert response.status_code == 404
    assert response.headers["content-type"].startswith("application/problem+json")
    assert response.json()["status"] == 404


def test_security_headers_are_present(client: TestClient) -> None:
    response = client.get("/api/v1/health")
    assert response.headers["x-content-type-options"] == "nosniff"
    assert response.headers["x-frame-options"] == "DENY"
