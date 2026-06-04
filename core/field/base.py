from abc import ABC, abstractmethod


class Field(ABC):
    def __init__(self, default=None, nullable=False):
        self.default = default
        self.nullable = nullable

    def __init_subclass__(cls):

        if cls.validate is Field.validate:
            raise TypeError(f"{cls.__name__} must implement validate()")

    def to_python(self, value):
        return value

    def __set_name__(self, owner, name):
        if hasattr(self, "name"):
            raise RuntimeError("Field instances cannot be reused")
        self.name = name
        self.attr = f"_{name}"

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.attr, self.default)

    def __set__(self, instance, value):
        if not self.nullable and value is None:
            raise ValueError(
                f"{instance.__class__.__name__}:{self.name} cannot be None."
            )
        value = self.to_python(value)
        self.validate(value)
        instance.__dict__[self.attr] = value

    @abstractmethod
    def validate(self, value):
        pass
