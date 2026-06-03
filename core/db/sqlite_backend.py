import sqlite3
from .backend import DatabaseBackend
from core.field.fields import IntField, CharField, FloatField

_TYPE_MAP = {IntField: "INTEGER", CharField: "TEXT", FloatField: "REAL"}

# SQLite will create a temporary db in memory
_SQLITE_TEMP_INMEMORY = ":memory:"


class SQLiteBackend(DatabaseBackend):
    def __init__(self, path: str = _SQLITE_TEMP_INMEMORY):
        self.conn = sqlite3.connect(path)
        self.conn.row_factory = (
            sqlite3.Row
        )  # Returns data["field"] instead of data[index]

    def execute(self, sql: str, params: tuple = ()) -> list[dict]:
        cur = self.conn.execute(sql, params)
        self.conn.commit()
        rows = cur.fetchall()
        return [dict(r) for r in rows] if rows else []

    def create_table(self, model) -> None:
        fields = model._fields
        cols = ", ".join(
            f"{name} {_TYPE_MAP.get(type(f), 'TEXT')}" for name, f in fields.items()
        )
        table = model.__name__.lower() + "s"
        self.execute(f"CREATE TABLE IF NOT EXISTS {table} ({cols})")

    def close(self) -> None:
        self.conn.close()
