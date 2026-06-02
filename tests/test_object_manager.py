from core.model.base import Model
from core.field.fields import IntField


def test_objects_are_model_specific():
    class A(Model):
        id = IntField()

    class B(Model):
        id = IntField()

    assert A.objects is not B.objects
