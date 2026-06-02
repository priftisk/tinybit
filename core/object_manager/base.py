from core.query.queryset import QuerySet


class ObjectManager:
    def __init__(self, model=None):
        self.model = model

    # def __get__(self, instance, owner):
    #     return QuerySet(self.model)

    def filter(self, **kwargs) -> QuerySet:
        return QuerySet(self.model).filter(**kwargs)

    def all(self) -> list:
        return QuerySet(self.model).all()

    def first(self):
        return QuerySet(self.model).first()

    def create(self, **kwargs):
        instance = self.model(**kwargs)
        is_valid = instance.full_clean()
        if is_valid:
            instance.save()
        return instance, is_valid
