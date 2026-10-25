"""Database engine and session factory (SQLite + SQLAlchemy)."""

from __future__ import annotations

import os
import sqlite3
from typing import Any

from sqlalchemy import Engine, create_engine, event
from sqlalchemy.orm import Session, sessionmaker

DATABASE_URL = os.environ.get("SHOP_DATABASE_URL", "sqlite:///shop.db")


@event.listens_for(Engine, "connect")
def _enable_sqlite_foreign_keys(dbapi_connection: Any, connection_record: Any) -> None:
    """Turn on FOREIGN KEY enforcement, which SQLite disables by default."""
    if isinstance(dbapi_connection, sqlite3.Connection):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON")
        cursor.close()


def create_db_engine(url: str = DATABASE_URL, *, echo: bool = False) -> Engine:
    """Create an engine for the given database URL."""
    return create_engine(url, echo=echo)


def create_session_factory(bind: Engine) -> sessionmaker[Session]:
    """Create a session factory bound to the engine."""
    return sessionmaker(bind=bind, autoflush=False, expire_on_commit=False)


engine = create_db_engine()
SessionLocal = create_session_factory(engine)
