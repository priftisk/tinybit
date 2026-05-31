from .queryset import QuerySet


class ObjectManager:
    def __get__(self, instance, owner):
        return QuerySet(owner)
