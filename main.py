from core.model.base import Model
from core.field.fields import IntField


class User(Model):
    id = IntField(default=1)
    age = IntField(default=20)


u = User(id="abc", age="x")

print(u.errors)
print(u.is_valid)
