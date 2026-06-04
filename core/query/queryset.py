from core.query.query import Query


class QuerySet:
    def __init__(self, model, filters={}):
        self.model = model
        self._filters = filters

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

    def get(self) -> list:
        db = self.model._db
        if db is None:
            raise RuntimeError(
                f"No backend configured. Call configure() before querying {self.model.__name__}."
            )
        query = self._build_query()

        rows = db.execute(query.raw, tuple(self._filters.values()))

        return [self.model(**row) for row in rows]

    def first(self):
        return self.all().get()[0]

    def all(self):
        return self._clone()

    def create(self, **kwargs):
        obj = self.model(**kwargs)
        return obj, obj.is_valid
