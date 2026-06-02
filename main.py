from core.model.base import Model
from core.field.fields import IntField, CharField


class Article(Model):
    id = IntField()
    title = CharField(max_length=140)
    body = CharField(max_length=255)


class User(Model):
    id = IntField()
    name = CharField(max_length=20)


qs = User.objects.filter(id=1).filter(name="Alice")

print(qs.execute())
