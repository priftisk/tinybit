from core.model.base import Model
from core.field.fields import IntField, CharField


class User(Model):
    id = IntField()
    age = IntField()


u = User(id="10", age=20)

print(u.id)  # 10 (int, not string)
print(u.age)  # 20
