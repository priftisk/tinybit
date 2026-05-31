from .base import Field


class IntField(Field):
    def to_python(self, value):
        if value is None:
            return None

        if isinstance(value, int):
            return value

        try:
            return int(value)
        except (TypeError, ValueError):
            raise TypeError("Cannot convert value to int")

    def validate(self, value):
        if not isinstance(value, int):
            raise TypeError("IntField must be int")


class CharField(Field):
    def __init__(self, default=None, max_length=255):
        self.max_length = max_length
        super().__init__(default)

    def validate(self, value):
        if len(value) > self.max_length:
            raise ValueError(
                f"Value too long for Charfield(max_length={self.max_length})"
            )


class FloatField(Field):
    def validate(self, value):
        if not isinstance(value, float):
            raise TypeError("FloatField must be float")
