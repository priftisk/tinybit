from core.model.base import *


class QuerySet:
    def __init__(self, model):
        self.model: Model = model
        self._filters = {}

    def filter(self, **kwargs):
        for kw in kwargs.keys():
            if kw not in self.model._fields:
                raise ValueError(f"Unknown field {kw} for {self.model.__name__}")
        self._filters.update(kwargs)
        return self  # For chaining

    def get(self, id: int):
        print(f"GET {id} from {self.model.__name__}")
        return None

    def all(self):
        return self
