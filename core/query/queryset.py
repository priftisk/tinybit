from core.query.query import Query


class QuerySet:
    def __init__(self, model, filters=None):
        self.model = model
        self._filters = filters or {}

    # -------------------------
    # internal helper
    # -------------------------
    def _clone(self, **kwargs):
        return QuerySet(self.model, {**self._filters, **kwargs})

    def _build_query(self):
        return Query(self.model, self._filters)

    # -------------------------
    # public API
    # -------------------------
    def filter(self, **kwargs):
        for k in kwargs:
            if k not in self.model._fields:
                raise ValueError(f"Unknown field {k}")
        return self._clone(**kwargs)

    def execute(self):
        return str(self._build_query())

    def all(self):
        return self.execute()

    def first(self):
        return self.execute()

    def create(self, **kwargs):
        obj = self.model(**kwargs)
        return obj, obj.is_valid
