from .base import Field


class IntField(Field):
    def validate(self, value):
        if not isinstance(value, int):
            raise TypeError("must be int")


class CharField(Field):
    def __init__(self, default=None, max_length=255):
        self.max_length = max_length
        super().__init__(default)

    def validate(self, value):
        if len(value) > self.max_length:
            raise ValueError(
                f"Value too long for Charfield(max_length={self.max_length})"
            )
        return super().validate(value)
