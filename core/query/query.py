class Query:
    def __init__(self, model, filters: dict):
        self._table: str = model._table
        self._model_fields: dict = model._fields
        self._raw_string: str = self._construct_raw_string(filters)

    def __str__(self):
        return self._raw_string

    def _construct_raw_string(self, filters: dict) -> str:
        s = "SELECT *\n"  # TODO use only() api for ObjectManager to specify columns
        s += f"FROM {self._table}\n"
        s += f"WHERE {" ".join([f"{name}={val}" for name, val in filters.items()])}"  # TODO string values need quotes
        s += ";"
        return s
