from core.model.base import Model
from core.field.base import IntField


class User(Model):
    id = IntField()
    age = IntField()


u = User()
u.age = 10
u.id = 1
print()
print(u)
