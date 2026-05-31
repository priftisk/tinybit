class FieldMeta(type):
    def __new__(cls, name, bases, namespace):
        if name != "Field" and "validate" not in namespace:
            raise TypeError(f"{name} is missing validate()")
        return super().__new__(cls, name, bases, namespace)


class Field(metaclass=FieldMeta):
    def __init__(self, default=None):
        self.default = default

    def __set_name__(self, owner, name):
        self.name = name
        self.attr = f"_{name}"

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name, self.default)

    def __safe_set__(self, instance, value):
        try:
            self.validate(value)
            instance.__dict__[self.name] = value

        except Exception as e:
            instance._errors[self.name] = str(e)

    def __set__(self, instance, value):
        self.__safe_set__(instance, value)

    def validate(self, value):
        pass
