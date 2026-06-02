class Field:
    def __init__(self, default=None):
        self.default = default

    def __init_subclass__(cls):
        super().__init_subclass__()

        if cls.validate is Field.validate:
            raise TypeError(f"{cls.__name__} must implement validate()")

    def to_python(self, value):
        return value

    def __set_name__(self, owner, name):
        self.name = name
        self.attr = f"_{name}"

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.attr, self.default)

    def __set__(self, instance, value):
        try:
            value = self.to_python(value)
            self.validate(value)
            # print(f"Setting {self.attr} to {value}")
            instance.__dict__[self.attr] = value
        except Exception as e:
            instance._errors[self.name] = str(e)

    def validate(self, value):
        pass
