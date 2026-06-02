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


user, created = User.objects.create(id=1, age=31, name=33)
user.full_clean()
user.save()
