from core.model.base import Model
from core.field.fields import IntField, CharField


def test_model_initialization():
    class User(Model):
        id = IntField()
        name = CharField(max_length=20)

    u = User(id=1, name="Alice")

    assert u.id == 1
    assert u.name == "Alice"


def test_model_equality():

    class User(Model):
        id = IntField()
        name = CharField(max_length=120)

    class Post(Model):
        id = IntField()
        title = CharField(max_length=144)

    u1 = User(id=1, name="Alice")
    p1 = Post(id=1, title="Some title")
    assert not u1 == p1


def test_to_dict():
    class User(Model):
        id = IntField()
        name = CharField(max_length=10)

    u = User(id=1, name="Alice")

    data = u.to_dict()

    assert data == {"id": 1, "name": "Alice"}
