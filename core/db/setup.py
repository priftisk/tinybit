from core.model.base import ModelBase, Model


def configure(backend) -> None:
    """
    Attach *backend* to every Model subclass that has been defined so far,
    creating their tables if they don't exist yet.
    """
    Model._db = backend
    for model_cls in ModelBase._registry:
        # backend.create_table(model_cls)
        print(model_cls)
