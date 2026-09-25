import pytest
from pydantic import ValidationError

from agentguard.core.config import Settings


def test_invalid_log_level_fails_clearly() -> None:
    with pytest.raises(ValidationError, match="AGENTGUARD_LOG_LEVEL"):
        Settings(
            DATABASE_URL="postgresql+psycopg://user:password@localhost:5432/db",
            REDIS_URL="redis://localhost:6379/0",
            AGENTGUARD_LOG_LEVEL="invalid",
        )
