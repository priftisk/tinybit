from core.model.base import Model
from core.field.fields import IntField, CharField
import pytest


def test_queryset_filter_valid_fields():
    class User(Model):
        id = IntField()
        name = CharField(max_length=20)

    qs = User.objects.filter(id=1, name="Alice")

    assert qs._filters == {"id": 1, "name": "Alice"}


def test_queryset_filter_invalid_field():
    class User(Model):
        id = IntField()

    with pytest.raises(ValueError):
        User.objects.filter(nonexistent=1)


def test_queryset_filter_chaining():
    class User(Model):
        id = IntField()
        name = CharField(max_length=20)

    qs = User.objects.filter(id=1).filter(name="Alice")

    assert qs._filters == {"id": 1, "name": "Alice"}


def test_queryset_get_generates_query(capsys):
    class User(Model):
        id = IntField()

    qs = User.objects.filter(id=1)

    qs.get()

    captured = capsys.readouterr().out

    assert "SELECT *" in captured
    assert "FROM users" in captured
    assert "id=1" in captured


def test_queryset_create_returns_instance():
    class User(Model):
        id = IntField()
        name = CharField(max_length=20)

    user, is_valid = User.objects.create(id=1, name="Alice")

    assert isinstance(user, User)
    assert isinstance(is_valid, bool)


def test_queryset_all_returns_self():
    class User(Model):
        id = IntField()

    qs = User.objects.all()

    assert qs is qs
