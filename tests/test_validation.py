from core.model.base import Model
from core.field.fields import IntField, CharField


def test_full_clean_valid_model():
    class User(Model):
        id = IntField()
        name = CharField(max_length=10)

    u = User(id=1, name="Alice")

    assert u.full_clean() is True
    assert u.errors == {}
