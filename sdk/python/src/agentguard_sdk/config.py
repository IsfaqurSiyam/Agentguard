from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class AgentGuardClientConfig:
    base_url: str
    timeout_seconds: float = 5.0
