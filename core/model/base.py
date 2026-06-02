from core.field.base import Field

from core.object_manager.base import ObjectManager


def _make_model_init(fields: dict):
    def __init__(self, **kwargs):
        setattr(self, "_errors", {})
        for name, field in fields.items():
            setattr(self, name, kwargs.get(name, field.default))

    return __init__


class Model:
    def __init_subclass__(cls):
        super().__init_subclass__()

        cls._fields = {k: v for k, v in cls.__dict__.items() if isinstance(v, Field)}

        if not hasattr(cls, "_table"):
            cls._table = cls.__name__.lower() + "s"

        cls.objects = ObjectManager()
        cls.__init__ = _make_model_init(cls._fields)

    @property
    def is_valid(self):
        return len(self.errors) == 0

    @property
    def errors(self):
        return self._errors

    def save(self):
        self.objects.save_to_db(self)

    def __repr__(self):
        field_str = ", ".join(
            f"{k}={getattr(self, k, None)!r}" for k in self.__class__._fields
        )
        return f"<{self.__class__.__name__}({field_str})>"

    def to_dict(self) -> dict:

        return {name: getattr(self, name) for name, _ in self._fields.items()}
