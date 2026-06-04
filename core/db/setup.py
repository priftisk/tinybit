from core.model.base import Model


def configure(backend, create_tables: bool = False) -> None:
    """
    Attach *backend* to every Model subclass that has been defined so far,
    creating their tables if they don't exist yet.
    """
    Model._db = backend
    if create_tables:
        for model_cls in Model._registry:
            if model_cls._table == None:
                continue
            backend.create_table(model_cls)
