from core.model.base import Model
from core.field.fields import IntField, CharField
from core.db.setup import configure
from core.db.sqlite_backend import SQLiteBackend
from core.util.parsers import model_from_csv

configure(SQLiteBackend("tinybit.db"), create_tables=False)


class User(Model):
    id = IntField()
    name = CharField(max_length=120)


new_user, is_valid = User.objects.create(id=2, name="Kostas")
if is_valid:
    new_user.save()  # Saves instance to db table

# Build query
all_users = User.objects.all()

print(all_users.get())


class SuperUser(User):  # Inherits User fields
    secret_code = CharField(default="admin")


super_user = SuperUser.objects.filter(secret_code="admin", name="Alex")
super_user.get()


class LogLine(Model):
    datetime = CharField(max_length=100)
    level = CharField(max_length=20)
    message = CharField(max_length=255)


for model in model_from_csv(LogLine, "fake_logs.csv"):
    print(
        model
    )  # LogLine(datetime='2026-01-01 14:56:15', level='DEBUG', message='File deleted')
