from core.model.base import Model
from core.field.fields import IntField, CharField
from core.db.setup import configure
from core.db.sqlite_backend import SQLiteBackend


class Article(Model):
    id = IntField()
    title = CharField(max_length=140)
    body = CharField(max_length=255)


class User(Model):
    id = IntField()
    name = CharField(max_length=20)
    age = IntField()


class Admin(User):  # Inherits fields from User class
    _table = None  # Prevents table creation during backend configuration
    admin_pass = CharField(default="admin", max_length=255)


configure(SQLiteBackend("tinybit.db"), create_tables=True)


all_users = User.objects.all()
some_users = User.objects.filter(age=22)
print(all_users.get(), some_users.get())

new_article, valid = Article.objects.create(id=1, title="Some title", body="Some body")
new_article.save()  # Saves to db
