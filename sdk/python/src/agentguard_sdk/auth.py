from typing import Protocol


class AuthenticationProvider(Protocol):
    """Reserved for future agent credentials; Phase 1 sends no credentials."""

    def headers(self) -> dict[str, str]: ...
