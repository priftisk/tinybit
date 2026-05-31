from core.field.base import Field


def _make_model_init(fields: dict):
    def __init__(self, **kwargs):
        setattr(self, "_errors", {})
        for name, field in fields.items():
            setattr(self, name, kwargs.get(name, field.default))

    return __init__


class ModelMeta(type):

    def __new__(cls, name, bases, namespace, /, **kwds):
        _fields = {k: v for k, v in namespace.items() if isinstance(v, Field)}
        new_cls = super().__new__(cls, name, bases, namespace, **kwds)
        new_cls._fields = _fields
        new_cls.__init__ = _make_model_init(_fields)

        return new_cls


class Model(metaclass=ModelMeta):

    @property
    def is_valid(self):
        return len(self.errors) == 0

    @property
    def errors(self):
        return self._errors

    def __repr__(self):
        field_str = ", ".join(
            f"{k}={getattr(self, k, None)!r}" for k in self.__class__._fields
        )
        return f"<{self.__class__.__name__}({field_str})>"

    def to_dict(self) -> dict:

        return {name: getattr(self, name) for name, _ in self._fields.items()}
