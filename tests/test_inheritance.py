from core.model.base import Model
from core.field.fields import IntField, CharField


def test_field_inheritance():
    class Base(Model):
        id = IntField()

    class User(Base):
        name = CharField(max_length=10)

    assert "id" in User._fields
    assert "name" in User._fields


def test_field_override():
    class Base(Model):
        id = IntField()

    class User(Base):
        id = CharField(max_length=10)

    assert isinstance(User._fields["id"], CharField)
