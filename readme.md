# tinybit

A lightweight Python ORM built using descriptors, metaclasses, and a query builder.
It supports model definitions, field validation, inheritance, serialization, a SQLite backend, and CSV parsing utilities.

---

## Quick Start

```python
from core.model.base import Model
from core.field.fields import IntField, CharField
from core.db.setup import configure
from core.db.sqlite_backend import SQLiteBackend

configure(SQLiteBackend("app.db"), create_tables=True)

class User(Model):
    id = IntField()
    name = CharField(max_length=120)

user, is_valid = User.objects.create(id=1, name="Alice")

if is_valid:
    user.save()

print(User.objects.all().get())
```

---

## Features

- Declarative model system
- Descriptor-based fields with validation
- Explicit validation via `full_clean()`
- Inheritance-aware models
- Object manager (`objects`)
- Query builder (`Query`, `QuerySet`)
- SQLite backend with pluggable backend abstraction
- `save()` persists instances to the configured database
- CSV-to-model parsing via `model_from_csv()`
- Serialization via `to_dict()`
- Pytest test suite

---

## Project Structure

```
tinybit/
│
├── core/
│   ├── field/
│   │   ├── base.py
│   │   └── fields.py
│   │
│   ├── model/
│   │   └── base.py
│   │
│   ├── object_manager/
│   │   └── base.py
│   │
│   ├── query/
│   │   ├── query.py
│   │   ├── query_builder.py
│   │   └── queryset.py
│   │
│   ├── db/
│   │   ├── setup.py
│   │   └── sqlite_backend.py
│   │
│   ├── util/
│   │   └── parsers.py
│   │
│   └── exceptions/
│       └── validation.py
│
├── tests/
│   ├── test_fields.py
│   ├── test_model_init.py
│   ├── test_validation.py
│   ├── test_inheritance.py
│   ├── test_to_dict.py
│   └── test_query.py
│
├── main.py
├── Makefile
└── README.md
```

---

## Installation

```bash
git clone https://github.com/priftisk/tinybit.git
cd tinybit
pip install pytest
```

---

## Running Tests

```bash
make test
```

Verbose:

```bash
pytest -v
```

---

## Models

### Defining Models

```python
from core.model.base import Model
from core.field.fields import IntField, CharField

class User(Model):
    id = IntField()
    name = CharField(max_length=120)
    age = IntField()
```

### Creating Instances

```python
user = User(id=1, name="Alice", age=25)
print(user)
```

### Validation

Validation is explicit using `full_clean()`:

```python
user = User(id="bad", name="Alice")

is_valid = user.full_clean()

print(user.is_valid)
print(user.errors)
```

### Saving

```python
user.save()  # Persists to the configured database
```

Automatically validates before saving.

### Serialization

```python
user.to_dict()
# {"id": 1, "name": "Alice", "age": 25}
```

---

## Database Backend

Configure a backend once at startup using `configure()`:

```python
from core.db.setup import configure
from core.db.sqlite_backend import SQLiteBackend

configure(SQLiteBackend("app.db"), create_tables=True)
```

Setting `create_tables=True` will create the database tables for all registered models automatically.
Setting it to `False` assumes the tables already exist.

---

## Inheritance

Models support field inheritance:

```python
class SuperUser(User):  # Inherits id and name from User
    secret_code = CharField(default="admin")

SuperUser.objects.filter(secret_code="admin", name="Alex").get()
```

---

## CSV Parsing

The `model_from_csv` utility maps CSV rows to model instances:

```python
from core.util.parsers import model_from_csv

class LogLine(Model):
    datetime = CharField(max_length=100)
    level = CharField(max_length=20)
    message = CharField(max_length=255)

for entry in model_from_csv(LogLine, "logs.csv"):
    print(entry)
# LogLine(datetime='2026-01-01 14:56:15', level='DEBUG', message='File deleted')
```

---

## Query System

The ORM includes a lightweight SQL-like query builder composed of `Query` and `QuerySet`.

### `filter(**kwargs)`

```python
User.objects.filter(id=1, name="Alice")
```

Validates field names against the model schema. Supports chaining:

```python
User.objects.filter(id=1).filter(name="Alice")
```

### `get()`

Builds and executes the query:

```python
User.objects.filter(id=1).get()
# User(id=1, name="Alice")
```

### `create(**kwargs)`

Creates and validates a model instance:

```python
user, is_valid = User.objects.create(id=1, name="Alice")
```

Returns the instance and the validation result.

### `all()`

Returns the full queryset:

```python
User.objects.all()
```

> **Note:** SQL parameter binding and injection protection are not yet implemented.

---

## Current Limitations

- No AND/OR grouping in filters
- No column selection (always queries `SELECT *`)
- No query result caching
- No result hydration from database rows back into model instances
