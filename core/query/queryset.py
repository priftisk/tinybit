from core.query.query import Query


class QuerySet:
    def __init__(self, model, filters={}, _only=set()):
        self.model = model
        self._filters = filters
        self._only = _only

    # -------------------------
    # internal helper
    # -------------------------
    def _clone(self, **kwargs):
        included_fields = self._only
        if "_only" in kwargs:
            included_fields = kwargs.get("_only", self._only)
            _ = kwargs.pop("_only")
        return QuerySet(
            self.model,
            {**self._filters, **kwargs},
            included_fields,
        )

    def _build_query(self):
        return Query(self.model, self._filters, self._only)

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

    def only(self, *args):
        return self._clone(_only=args)
        # self._only.add(next(arg for arg in args))

    def first(self):
        return self.all().get()[0]

    def all(self):
        return self._clone()

    def create(self, **kwargs):
        obj = self.model(**kwargs)
        return obj, obj.is_valid
