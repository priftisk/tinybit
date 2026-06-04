from core.query.queryset import QuerySet


class ObjectManager:
    def __init__(self, model=None):
        self.model = model

    def filter(self, **kwargs) -> QuerySet:
        return QuerySet(self.model).filter(**kwargs)

    def all(self) -> list:
        return QuerySet(self.model).all()

    def first(self):
        return QuerySet(self.model).first()

    def create(self, *args, **kwargs):
        if args and not kwargs:
            raise Exception(
                f"{self.__class__.__name__}.create() must use keyword arguments."
            )
        instance = self.model(**kwargs)
        is_valid = instance.full_clean()
        return instance, is_valid
