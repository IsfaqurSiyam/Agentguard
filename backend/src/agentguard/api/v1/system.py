"""Non-authoritative foundation endpoints."""

from typing import cast

from fastapi import APIRouter, Depends, HTTPException, Request, status
from pydantic import BaseModel
from redis.asyncio import Redis
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncEngine

router = APIRouter(tags=["system"])


class HealthResponse(BaseModel):
    status: str
    service: str
    version: str
    request_id: str | None


def get_engine(request: Request) -> AsyncEngine:
    return cast(AsyncEngine, request.app.state.db_engine)


def get_redis(request: Request) -> Redis:
    return cast(Redis, request.app.state.redis)


@router.get("/health", response_model=HealthResponse)
async def health(request: Request) -> HealthResponse:
    return HealthResponse(
        status="ok",
        service="agentguard-gateway",
        version="0.1.0",
        request_id=request.headers.get("x-request-id"),
    )


@router.get("/ready", response_model=HealthResponse)
async def ready(
    request: Request,
    engine: AsyncEngine = Depends(get_engine),
    redis: Redis = Depends(get_redis),
) -> HealthResponse:
    try:
        async with engine.connect() as connection:
            await connection.execute(text("SELECT 1"))
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail="Database is unavailable."
        ) from exc
    try:
        await redis.ping()
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail="Redis is unavailable."
        ) from exc
    return HealthResponse(
        status="ready",
        service="agentguard-gateway",
        version="0.1.0",
        request_id=request.headers.get("x-request-id"),
    )
