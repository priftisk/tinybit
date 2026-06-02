import sqlite3
from .backend import DatabaseBackend
from core.field.fields import IntField, CharField

_TYPE_MAP = {
    IntField: "INTEGER",
    CharField: "TEXT",
}


class SQLiteBackend(DatabaseBackend):

    def __init__(self, path: str = ":memory:"):
        self.conn = sqlite3.connect(path)
        self.conn.row_factory = sqlite3.Row

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
