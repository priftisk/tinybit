from core.model.base import Model
from core.field.fields import IntField, CharField
from core.db.setup import configure
from core.db.sqlite_backend import SQLiteBackend

configure(SQLiteBackend("tinybit.db"))


class Article(Model):
    id = IntField()
    title = CharField(max_length=140)
    body = CharField(max_length=255)


class User(Model):
    id = IntField()
    name = CharField(max_length=20)
    age = IntField()


# print(User._registry)
new_user = User.objects.all().get()
print(new_user)
