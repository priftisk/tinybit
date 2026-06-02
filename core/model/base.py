from core.field.base import Field


class ModelBase(type):
    """
    Metaclass that:
      1. Collects Field descriptors into cls._fields at class creation time.
      2. Registers every concrete subclass of Model in ModelMeta._registry
         so configure() can iterate them and create their tables automatically.
      3. Attaches an ObjectManager as cls.objects.
    """

    # All concrete Model subclasses register here at class-definition time.
    _registry: list = []

    def __new__(mcs, name, bases, namespace):
        fields = {
            key: value for key, value in namespace.items() if isinstance(value, Field)
        }

        inherited_fields = {}
        for base in bases:
            if hasattr(base, "_fields"):
                inherited_fields.update(base._fields)

        namespace["_fields"] = {**inherited_fields, **fields}
        namespace.setdefault("_table", f"{name.lower()}s")

        cls = super().__new__(mcs, name, bases, namespace)

        if name != "Model":
            mcs._registry.append(cls)

            from core.object_manager.base import ObjectManager

            cls.objects = ObjectManager(cls)

        return cls


class Model(metaclass=ModelBase):
    """
    Base class for all models.

    _db is shared across the whole class hierarchy: setting Model._db
    (via configure()) makes it visible on every subclass without having
    to set it per-class.
    """

    _db = None  # set once by configure(); inherited by all subclasses

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.is_valid: bool | None = None
        self.errors: dict = {}

    def full_clean(self) -> bool:
        self.errors = {}
        for name, field in self.__class__._fields.items():
            value = getattr(self, name, None)
            try:
                field.validate(value)
            except Exception as e:
                self.errors[name] = str(e)
        return not self.errors

    def save(self) -> None:
        if not self.full_clean():
            raise Exception(self.errors)
        db = self.__class__._db
        if db is None:
            raise RuntimeError(
                "No backend configured. Call configure() before calling save()."
            )
        data = self.to_dict()
        cols = ", ".join(data.keys())
        placeholders = ", ".join(["?"] * len(data))
        table = self.__class__.__name__.lower() + "s"
        db.execute(
            f"INSERT INTO {table} ({cols}) VALUES ({placeholders})",
            tuple(data.values()),
        )

    def to_dict(self) -> dict:
        return {name: getattr(self, name, None) for name in self.__class__._fields}

    def __repr__(self):
        fields = ", ".join(f"{k}={v!r}" for k, v in self.to_dict().items())
        return f"{self.__class__.__name__}({fields})"
