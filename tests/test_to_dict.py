from core.model.base import Model
from core.field.fields import IntField, CharField


def test_to_dict():
    class User(Model):
        id = IntField()
        name = CharField(max_length=10)

    u = User(id=1, name="Alice")

    data = u.to_dict()

    assert data == {"id": 1, "name": "Alice"}
