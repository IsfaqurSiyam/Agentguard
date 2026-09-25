from __future__ import annotations

from typing import cast

import httpx

from agentguard_sdk.config import AgentGuardClientConfig


class AgentGuardClient:
    """Minimal SDK client. Tool execution is deliberately not implemented."""

    def __init__(self, config: AgentGuardClientConfig) -> None:
        self._config = config

    def health(self) -> dict[str, object]:
        response = httpx.get(
            f"{self._config.base_url.rstrip('/')}/health", timeout=self._config.timeout_seconds
        )
        response.raise_for_status()
        return cast(dict[str, object], response.json())
