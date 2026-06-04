from core.model.base import Model
from core.db.backend import DatabaseBackend


def configure(backend, create_tables: bool = False) -> None:
    """
    Attach *backend* to every Model subclass that has been defined so far,
    creating their tables if they don't exist yet.
    """
    if not isinstance(backend, DatabaseBackend):  # Reject invalid database type
        raise RuntimeError(
            f"Backend must be a DatabaseBackend class. Found: {backend.__class__.__name__}"
        )
    if Model._db is not None:  # Configure was called twice, Reject the second backend.
        raise RuntimeError(
            f"Could not configure {backend.__class__.__name__} because another backend has already been configured. Found: {Model._db.__class__.__name__}"
        )
    Model._db = backend
    if create_tables:
        for model_cls in Model._registry:
            if model_cls._table is None:
                continue
            backend.create_table(model_cls)
