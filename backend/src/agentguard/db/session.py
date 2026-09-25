"""Database engine and transaction boundaries."""

from __future__ import annotations

from collections.abc import AsyncIterator

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from agentguard.core.config import Settings


def build_engine(settings: Settings) -> AsyncEngine:
    return create_async_engine(str(settings.database_url), pool_pre_ping=True)


def build_session_factory(settings: Settings) -> async_sessionmaker[AsyncSession]:
    return async_sessionmaker(build_engine(settings), expire_on_commit=False)


async def session_scope(factory: async_sessionmaker[AsyncSession]) -> AsyncIterator[AsyncSession]:
    async with factory() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
