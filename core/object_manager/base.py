from core.query.queryset import QuerySet


class ObjectManager:
    def __init__(self, model=None):
        self.model = model

    def __get__(self, instance, owner):
        return QuerySet(owner)

    def save_to_db(self, obj):
        print(f"Saving {obj} to DB")
