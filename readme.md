# Mini ORM

A lightweight Python ORM-like system built using descriptors, metaclasses, and a simple query builder.
It supports model definitions, field validation, inheritance, serialization, and a basic SQL-like query layer.


---

## Quick start
```python
from tinybit import *

class User(Model):
    id = IntField()
    name = CharField(max_length=20)

configure(SQLiteBackend("app.db"), create_tables=True)

user, _ = User.objects.create(
    id=1,
    name="John"
)

user.save()

print(User.objects.all().get())
```

---

## Features

* Declarative model system
* Descriptor-based fields with validation
* Explicit validation via `full_clean()`
* Inheritance-aware models
* Object manager (`objects`)
* Query builder (`Query`, `QueryBuilder`, `QuerySet`)
* SQL-like query generation (string-based)
* Serialization via `to_dict()`
* Pytest test suite

---

## Project Structure

```text
project/
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
├── Makefile
└── README.md
```

---

## Installation

```bash
git clone <repo-url>
cd <project-folder>
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

# Models

## Defining Models

```python
from core.model.base import Model
from core.field.fields import IntField, CharField


class User(Model):
    id = IntField()
    name = CharField(max_length=20)
    age = IntField()
```

---

## Creating Instances

```python
user = User(id=1, name="Alice", age=25)
print(user)
```

---

## Validation

Validation is explicit using `full_clean()`:

```python
user = User(id="bad", name="Alice")

is_valid = user.full_clean()

print(user.is_valid)
print(user.errors)
```

---

## Saving

```python
user.save()
```

Automatically validates before saving.

---

## Serialization

```python
user.to_dict()
```

Output:

```python
{"id": 1, "name": "Alice", "age": 25}
```

---

# Query System

The ORM includes a lightweight SQL-like query builder.

It is composed of:

* `Query`
* `QueryBuilder`
* `QuerySet`

---

## Query

Generates raw SQL-like strings from filters.

Example output:

```sql
SELECT *
FROM users
WHERE id=1 name=Alice;
```

> Note: string escaping and SQL injection protection are not implemented yet.

---

## QueryBuilder (Currently unused)

Responsible for constructing and caching queries.

```python
qb = QueryBuilder(User, {"id": 1})
print(qb.query)
```

Lazy evaluation is used (query is built only when accessed).

---

## QuerySet API

Accessible via `Model.objects`.

---

### filter(**kwargs)

```python
User.objects.filter(id=1, name="Alice")
```

Validates field names against model schema.

Supports chaining:

```python
User.objects.filter(id=1).filter(name="Alice")
```

---

### get()

Builds and prints the SQL query:

```python
User.objects.filter(id=1).get()
```

Example output:

```sql
SELECT *
FROM users
WHERE id=1;
```

---

### create(**kwargs)

Creates and validates a model instance:

```python
user, is_valid = User.objects.create(id=1, name="Alice")
```

Returns:

* instance
* validation result

---

### all()

Returns the queryset unchanged:

```python
User.objects.all()
```

---

## Current Limitations

* No real database execution layer
* No result hydration into models
* No SQL parameter binding
* No AND/OR grouping in filters
* No column selection (currently always queries all columns)
* No query result caching
* No backend abstraction




