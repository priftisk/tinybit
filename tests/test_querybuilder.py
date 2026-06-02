from core.query.query_builder import QueryBuilder


def test_query_builder_lazy_creation():
    class FakeModel:
        _table = "users"
        _fields = {"id": None}

    qb = QueryBuilder(FakeModel, {"id": 1})

    # should not exist yet (lazy)
    assert qb._query is None

    # triggers construction
    query = qb.query

    assert query is not None
    assert "FROM users" in str(query)
