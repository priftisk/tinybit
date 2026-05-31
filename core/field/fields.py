from .base import Field


class IntField(Field):
    def validate(self, value):
        if not isinstance(value, int):
            raise TypeError("must be int")
