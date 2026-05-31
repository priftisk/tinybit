from core.model.base import Model
from core.field.fields import IntField, CharField


class User(Model):
    id = IntField()
    age = IntField()
    name = CharField(max_length=20)


# u = User(id=3, age=20, name="Kostas")
User.objects.filter(name="Kostas").filter(age=20)
# User.objects.get(id=3)

u, success = User.objects.create(id=1, name="Mario", age="5")
print(u, success)
