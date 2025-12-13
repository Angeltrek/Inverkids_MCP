from contextlib import contextmanager
from typing import Any, Dict, Iterator, List, Optional
import os

import psycopg2
from psycopg2.extras import RealDictCursor

from src.utils.errors import DatabaseConnectionError

def _get_db_config() -> Dict[str, Any]:
    try:
        return {
            "host": os.environ["DB_HOST"],
            "port": int(os.environ.get("DB_PORT", 5432)),
            "dbname": os.environ["DB_NAME"],
            "user": os.environ["DB_USER"],
            "password": os.environ["DB_PASSWORD"],
            "sslmode": os.environ.get("DB_SSLMODE", "require"),
        }
    except KeyError as exc:
        raise DatabaseConnectionError(
            f"Missing database environment variable: {exc}"
        ) from exc

@contextmanager
def get_db_connection() -> Iterator[Any]:
    """
    Context manager that yields a PostgreSQL connection.

    Ensures proper cleanup and is safe for Lambda usage.
    """
    config = _get_db_config()

    conn = None
    try:
        conn = psycopg2.connect(**config)
        yield conn
    except psycopg2.Error as exc:
        raise DatabaseConnectionError(str(exc)) from exc
    finally:
        if conn is not None:
            conn.close()

def execute_query(
    query: str,
    params: Optional[Dict[str, Any]] = None,
) -> List[Dict[str, Any]]:
    """
    Execute a read-only SQL query and return rows as dictionaries.
    """
    with get_db_connection() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(query, params)
            return cursor.fetchall()
