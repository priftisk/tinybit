from core.field.base import Field


class ModelMeta(type):
    def __new__(cls, name, bases, namespace, /, **kwds):
        _fields = {k: v for k, v in namespace.items() if isinstance(v, Field)}
        new_cls = super().__new__(cls, name, bases, namespace, **kwds)
        new_cls._fields = _fields
        return new_cls


class Model(metaclass=ModelMeta):

    def __repr__(self):
        field_str = ", ".join(
            f"{k}={getattr(self, k, None)!r}" for k in self.__class__._fields
        )
        return f"<{self.__class__.__name__}({field_str})>"

    def to_dict(self) -> dict:

        return {name: getattr(self, name) for name, _ in self._fields.items()}
