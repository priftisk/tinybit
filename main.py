from core.model.base import Model
from core.field.fields import IntField, CharField


class User(Model):
    id = IntField(default=1)
    age = IntField(default=20)
    name = CharField(max_length=10, default="sbuiad")


u = User()

print(u.errors)
print(u)
