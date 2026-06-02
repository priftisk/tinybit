class Query:
    def __init__(self, model, filters: dict):
        self._table = model._table
        self._raw_string = self._build(filters)

    def __str__(self):
        return self._raw_string

    def _build(self, filters):
        sql = "SELECT *\n"
        sql += f"FROM {self._table}\n"

        if filters:
            sql += "WHERE " + " ".join(f"{k}={v}" for k, v in filters.items())

        sql += ";"
        return sql
