from core.query.query import Query


class QueryBuilder:
    def __init__(self, model, filters: dict):
        self._model = model
        self._filters: dict = filters
        self._query = self._construct_query()

    def _construct_query(self) -> Query:
        q = Query(self._model, self._filters)
        print("Constructing: ", q)
        return q
