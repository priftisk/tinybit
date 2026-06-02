import pytest
from core.field.base import Field
from core.field.fields import IntField, CharField, BoolField


def test_field_default_assignment():
    f = IntField(default=10)

    class M:
        x = f

    m = M()
    assert m.x == 10


def test_charfield_accepts_string():
    f = CharField(max_length=10)

    class M:
        x = f

    m = M()
    m.x = "hello"
    assert m.x == "hello"


def test_intfield_rejects_invalid_value():
    f = IntField("not-an-int")

    class M:
        x = f

    m = M()

    with pytest.raises(Exception):
        m.x = "not-an-int"


def test_boolfield_rejects_invalid_value():
    f = BoolField("not-a-bool")

    class M:
        x = f

    m = M()

    with pytest.raises(Exception):
        m.x = "not-a-bool"
