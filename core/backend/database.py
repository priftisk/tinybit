from core.backend.base import DatabaseBackend
import sqlite3


class SQLiteBackend(DatabaseBackend):
    def __init__(self, path: str):
        self._path: str = path
        self._conn: sqlite3.Connection = sqlite3.connect(path)

    def select(self, query):
        db = self._conn.cursor()
        res = db.execute(query)
        return res.fetchall()
