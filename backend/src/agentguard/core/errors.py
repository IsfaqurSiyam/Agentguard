"""Stable API error responses."""

from __future__ import annotations

from typing import Any

from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException


def problem_response(
    request: Request, status: int, title: str, detail: str, errors: list[Any] | None = None
) -> JSONResponse:
    payload: dict[str, Any] = {
        "type": f"https://agentguard.dev/problems/{title.lower().replace(' ', '-')}",
        "title": title,
        "status": status,
        "detail": detail,
        "instance": str(request.url.path),
        "request_id": request.headers.get("x-request-id"),
    }
    if errors is not None:
        payload["errors"] = errors
    return JSONResponse(status_code=status, content=payload, media_type="application/problem+json")


async def http_exception_handler(request: Request, exc: StarletteHTTPException) -> JSONResponse:
    return problem_response(request, exc.status_code, "Request failed", str(exc.detail))


async def validation_exception_handler(
    request: Request, exc: RequestValidationError
) -> JSONResponse:
    return problem_response(
        request, 422, "Validation failed", "Request validation failed.", list(exc.errors())
    )


async def unhandled_exception_handler(request: Request, _exc: Exception) -> JSONResponse:
    return problem_response(request, 500, "Internal server error", "An unexpected error occurred.")
