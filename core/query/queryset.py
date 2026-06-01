from core.query.query_builder import QueryBuilder


class QuerySet:
    def __init__(self, model):
        self.model = model
        self.data = []
        self._filters = {}

    def save_to_db(self, valid_model):
        print(f"Commiting {valid_model} to db")

    def filter(self, **kwargs):
        for kw in kwargs.keys():
            if kw not in self.model._fields:
                raise ValueError(f"Unknown field {kw} for {self.model.__name__}")
        self._filters.update(kwargs)
        return self  # For chaining

    def get(self):
        if not self.data:
            qb = QueryBuilder(self.model, self._filters)
            print(qb.query._raw_string)

        return self.data

    def create(self, **kwargs):
        new = None
        valid = True
        try:
            new = self.model(**kwargs)
            if not new.is_valid:
                new = None
                valid = False
        except Exception as e:
            raise e
        return new, valid

    def all(self):
        return self
