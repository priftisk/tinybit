from core.query.query import Query


class QueryBuilder:
    def __init__(self, model, filters: dict):
        self._model = model
        self._filters: dict = filters
        self._query = None

    @property
    def query(self):
        return self._query

    @query.getter
    def query(self):
        if not self._query:
            self._query = self._construct_query()
        return self._query

    def _construct_query(self) -> Query:
        q = Query(self._model, self._filters)
        return q
