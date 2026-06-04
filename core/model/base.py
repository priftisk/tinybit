from core.field.base import Field


class Model:
    _registry = []
    _db = None

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

        # Collect inherited fields
        inherited_fields = {}
        for base in cls.__bases__:
            if hasattr(base, "_fields"):
                inherited_fields.update(base._fields)

        # Collect fields declared on this class
        fields = {
            key: value
            for key, value in cls.__dict__.items()
            if isinstance(value, Field)
        }

        cls._fields = {**inherited_fields, **fields}

        if not hasattr(cls, "_table"):
            cls._table = f"{cls.__name__.lower()}s"
        elif (
            getattr(cls, "_table") == None
        ):  # User explicitly set it None in their defined Model subclass(will be ignored during table creation)
            cls._table = None

        # Register class so it can be used to create tables in db
        Model._registry.append(cls)

        from core.object_manager.base import ObjectManager

        cls.objects = ObjectManager(cls)

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

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

    def __eq__(self, other):
        if not isinstance(other, Model):
            return False
        return self.__class__.__name__ == other.__class__.__name__

    def __repr__(self):
        fields = ", ".join(f"{k}={v!r}" for k, v in self.to_dict().items())
        return f"{self.__class__.__name__}({fields})"
