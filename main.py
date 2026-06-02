from core.model.base import Model
from core.field.fields import IntField, CharField


class User(Model):
    id = IntField()
    age = IntField()
    name = CharField(max_length=20)


class Article(Model):
    id = IntField()
    title = CharField(max_length=140)
    body = CharField(max_length=255)


user = User(id=1, name="Alice", age=25)
print(user)
