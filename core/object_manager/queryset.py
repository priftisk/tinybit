class QuerySet:
    def __init__(self, model):
        self.model = model
        self._filters = {}

    def filter(self, **kwargs):
        self._filters.update(kwargs)
        return self  # For chaining

    def get(self, id: int):
        print(f"GET {id} from {self.model.__name__}")
        return None

    def all(self):
        return self
