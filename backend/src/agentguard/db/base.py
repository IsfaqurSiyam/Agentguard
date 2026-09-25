"""Future tenant-scoped SQLAlchemy entities inherit from this base."""

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass
