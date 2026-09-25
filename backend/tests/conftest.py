import os
from collections.abc import Iterator

import pytest
from fastapi.testclient import TestClient

# The module-level ASGI entry point validates configuration, as it should in a
# deployed process. Tests provide harmless local endpoints before importing it.
os.environ.setdefault(
    "DATABASE_URL", "postgresql+psycopg://user:password@localhost:5432/agentguard_test"
)
os.environ.setdefault("REDIS_URL", "redis://localhost:6379/15")
os.environ.setdefault("AGENTGUARD_CORS_ORIGINS", "http://localhost:3000")

from agentguard.core.config import Settings
from agentguard.main import create_app


@pytest.fixture
def settings() -> Settings:
    return Settings(
        DATABASE_URL="postgresql+psycopg://user:password@localhost:5432/agentguard_test",
        REDIS_URL="redis://localhost:6379/15",
        AGENTGUARD_CORS_ORIGINS=["http://localhost:3000"],
    )


@pytest.fixture
def client(settings: Settings) -> Iterator[TestClient]:
    with TestClient(create_app(settings)) as test_client:
        yield test_client
