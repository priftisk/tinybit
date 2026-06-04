class Query:
    def __init__(self, model, filters: dict, columns: set):
        self._model = model
        self._raw_string = self._build(filters, columns)

    @property
    def raw(self):
        return self._raw_string

    def _build(self, filters, columns):
        cols = "*" if not columns else " ,".join(col for col in columns)
        sql = f"SELECT {cols} FROM {self._model._table}\n"
        where = " AND ".join(f"{k}=?" for k in filters)
        if where:
            sql += f"WHERE {where}"
        sql += ";"
        return sql
