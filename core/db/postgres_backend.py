import psycopg2
from core.db.backend import DatabaseBackend
from contextlib import contextmanager


class PostgresBackend(DatabaseBackend):
    def __init__(self, conn_string: str):
        self._conn_string = conn_string
        self.conn = None
        # self.conn = psycopg2.connect(conn_string)

    @contextmanager
    def _cursor(self):
        try:
            if not self.conn:
                self.conn = psycopg2.connect(self._conn_string)
            cur = self.conn.cursor()
            yield cur
        except psycopg2.errors.Error as e:
            raise e
        finally:
            cur.close()
            self.conn.close()

    def close(self):
        if self.conn:
            self.conn.close()

    def execute(self, sql: str, params: tuple = ()) -> list[dict]:
        rows = []
        with self._cursor() as cur:
            cur.execute(sql, params)
            self.conn.commit()
            rows = cur.fetchall()

        return [dict(r) for r in rows] if rows else []

    def create_table(self, model_class):
        "CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);"
        return super().create_table(model_class)
