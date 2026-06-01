class Query:
    def __init__(self, model, filters: dict):
        self._table: str = model._table
        self._model_fields: dict = model._fields
        self._raw_string: str = self._construct_raw_string(filters)

    def _construct_raw_string(self, filters: dict) -> str:
        s = "SELECT *"  # TODO use only() api for ObjectManager to specify columns
        s += f"FROM {self._table}"
        for name, val in filters.items():
            print(name, val)

        """
        SELECT c1.CustomerName, c1.Country
FROM Customer AS c1, Customer AS c2
WHERE c1.Age = c2.Age AND c1.Country = c2.Country;
        """
