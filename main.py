from core.model.base import Model
from core.field.fields import IntField, CharField
from core.backend.database import SQLiteBackend

backend = SQLiteBackend("tinybit.db")


class Article(Model):
    id = IntField()
    title = CharField(max_length=140)
    body = CharField(max_length=255)


class User(Model):
    id = IntField()
    name = CharField(max_length=20)
    age = IntField()


qs = User.objects.all()
print(qs)
data = backend.select(qs)
print(data)
