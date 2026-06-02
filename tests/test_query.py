from core.query.query import Query


def test_query_builds_basic_select():
    class FakeModel:
        _table = "users"
        _fields = {"id": None, "name": None}

    q = Query(FakeModel, {"id": 1, "name": "Alice"})

    sql = str(q.raw)

    assert "SELECT *" in sql
    assert "FROM users" in sql
    assert "id=1" in sql
    assert "name=Alice" in sql
    assert sql.endswith(";")
