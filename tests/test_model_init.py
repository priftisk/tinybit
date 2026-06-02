from core.model.base import Model
from core.field.fields import IntField, CharField


def test_model_initialization():
    class User(Model):
        id = IntField()
        name = CharField(max_length=20)

    u = User(id=1, name="Alice")

    assert u.id == 1
    assert u.name == "Alice"
