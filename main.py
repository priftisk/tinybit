from core.model.base import Model
from core.field.fields import IntField, CharField


class User(Model):
    id = IntField()
    age = IntField()
    name = CharField(max_length=20)


u = User(id=3, age=20, name="Kostas")

# u.get(id=3)
# print(dir(User.objects))
