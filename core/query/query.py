class Query:
    def __init__(self, model, filters: dict):
        self._model = model
        self._raw_string = self._build(filters)

    @property
    def raw(self):
        return self._raw_string

    # def __str__(self):
    #     return self._raw_string

    def _build(self, filters):
        where = " AND ".join(f"{k}=?" for k in filters)
        sql = f"SELECT * FROM {self._model._table} WHERE {where}"
        return sql
