"""Configuration with explicit, fail-fast validation."""

from __future__ import annotations

from functools import lru_cache
from typing import Annotated, Literal

from pydantic import AnyHttpUrl, Field, PostgresDsn, RedisDsn, field_validator
from pydantic_settings import BaseSettings, NoDecode, SettingsConfigDict


class Settings(BaseSettings):
    """Runtime configuration. Environment variables are the source of truth."""

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    environment: Literal["development", "test", "production"] = Field(
        default="development", validation_alias="AGENTGUARD_ENV"
    )
    log_level: str = Field(default="INFO", validation_alias="AGENTGUARD_LOG_LEVEL")
    database_url: PostgresDsn = Field(validation_alias="DATABASE_URL")
    redis_url: RedisDsn = Field(validation_alias="REDIS_URL")
    cors_origins: Annotated[list[AnyHttpUrl], NoDecode] = Field(
        default_factory=list, validation_alias="AGENTGUARD_CORS_ORIGINS"
    )

    @field_validator("cors_origins", mode="before")
    @classmethod
    def split_cors_origins(cls, value: object) -> object:
        if isinstance(value, str):
            return [item.strip() for item in value.split(",") if item.strip()]
        return value

    @field_validator("log_level")
    @classmethod
    def validate_log_level(cls, value: str) -> str:
        normalized = value.upper()
        if normalized not in {"CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG"}:
            raise ValueError("AGENTGUARD_LOG_LEVEL must be a standard logging level")
        return normalized


@lru_cache
def get_settings() -> Settings:
    return Settings()  # type: ignore[call-arg]
