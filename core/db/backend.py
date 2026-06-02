from abc import ABC, abstractmethod


class DatabaseBackend(ABC):

    @abstractmethod
    def execute(self, sql: str, params: tuple = ()) -> list[dict]:
        """Execute a query and return rows as dicts."""
        ...

    @abstractmethod
    def create_table(self, model_class) -> None:
        """Create the table for a model if it doesn't exist."""
        ...

    @abstractmethod
    def close(self) -> None: ...
