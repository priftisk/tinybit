# Mini ORM

A lightweight Python ORM-like system built using descriptors, metaclasses, and a simple query builder.
It supports model definitions, field validation, inheritance, serialization, and a basic SQL-like query layer.

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

```text id="s1xq9m"
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

```bash id="k8xw0p"
git clone <repo-url>
cd <project-folder>
pip install pytest
```

---

## Running Tests

```bash id="b9q1ds"
make test
```

Verbose:

```bash id="c0p8lw"
pytest -v
```

---

# Models

## Defining Models

```python id="l2xv9a"
from core.model.base import Model
from core.field.fields import IntField, CharField


class User(Model):
    id = IntField()
    name = CharField(max_length=20)
    age = IntField()
```

---

## Creating Instances

```python id="q7v0zd"
user = User(id=1, name="Alice", age=25)
print(user)
```

---

## Validation

Validation is explicit using `full_clean()`:

```python id="m3z8qa"
user = User(id="bad", name="Alice")

is_valid = user.full_clean()

print(user.is_valid)
print(user.errors)
```

---

## Saving

```python id="r1k9cw"
user.save()
```

Automatically validates before saving.

---

## Serialization

```python id="n8p4sd"
user.to_dict()
```

Output:

```python id="v2l0xn"
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

```sql id="u2q1wm"
SELECT *
FROM users
WHERE id=1 name=Alice;
```

> Note: string escaping and SQL injection protection are not implemented yet.

---

## QueryBuilder

Responsible for constructing and caching queries.

```python id="z9m2qa"
qb = QueryBuilder(User, {"id": 1})
print(qb.query)
```

Lazy evaluation is used (query is built only when accessed).

---

## QuerySet API

Accessible via `Model.objects`.

---

### filter(**kwargs)

```python id="c8n2pl"
User.objects.filter(id=1, name="Alice")
```

Validates field names against model schema.

Supports chaining:

```python id="x0v9qa"
User.objects.filter(id=1).filter(name="Alice")
```

---

### get()

Builds and prints the SQL query:

```python id="y9q3sd"
User.objects.filter(id=1).get()
```

Example output:

```sql id="t8m1za"
SELECT *
FROM users
WHERE id=1;
```

---

### create(**kwargs)

Creates and validates a model instance:

```python id="k2v8sn"
user, is_valid = User.objects.create(id=1, name="Alice")
```

Returns:

* instance
* validation result

---

### all()

Returns the queryset unchanged:

```python id="w1q9mz"
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




