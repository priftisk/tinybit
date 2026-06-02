from core.query.queryset import QuerySet

# class ObjectManagerBase(type):
#     def __new__(cls, name, bases, namespace, /, **kwds):
#         return super().__new__(name, bases, namespace, **kwds)


class ObjectManager:
    def __init__(self, model=None, backend=None):
        self.model = model
        self.backend = backend

    def __get__(self, instance, owner):
        return QuerySet(owner, self.backend)
