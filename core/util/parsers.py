from core.model.base import Model


def _read(file):
    for line in file.readlines():
        yield line


def _proccess_line(line):
    line = line.strip()
    if line:
        args = line.split(",")
        yield args


def _map_to_model(model_cls, model_fields, args):
    kwargs = {k: v for k, v in zip(model_fields, args)}
    new_cls = model_cls.objects.create(**kwargs)
    yield new_cls


# Creates a generator that yields each line of the csv as the desired model.
def model_from_csv(model_cls, csv_path):
    if model_cls is Model:
        raise ValueError("Cannot use base Model.")

    try:
        model_fields = list(model_cls._fields.keys())
        with open(csv_path, "r") as f:
            for line in _read(f):
                args = _proccess_line(line)
                model = _map_to_model(model_cls, model_fields, next(args))
                yield from model
    except Exception as e:  # TODO
        raise e
