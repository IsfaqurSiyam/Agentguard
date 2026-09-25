"""Minimal Redis boundary; jobs and rate limits belong behind this interface."""

from __future__ import annotations

from typing import cast

from redis.asyncio import Redis

from agentguard.core.config import Settings


def build_redis(settings: Settings) -> Redis:
    return cast(
        Redis, Redis.from_url(str(settings.redis_url), encoding="utf-8", decode_responses=True)
    )
