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


# user = User(id="dsas", name=231)
user, created = User.objects.create(id="dsas", name=231)
print(user.errors)

# article, created = Article.objects.create(
#     id=12, title="The article title", body="The article body"
# )

# u = User.objects.filter(id=1, name="dsad")
# u.get()

# a = Article.objects.filter(title="Some title")
# a.get()
