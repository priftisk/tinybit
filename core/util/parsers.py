from core.model.base import Model


# Create the desired models from csv data file.
def from_csv(model_cls, csv_path):
    if model_cls is Model:
        raise ValueError("Cannot use base Model.")
    data = []
    model_fields = list(model_cls._fields.keys())
    try:
        with open(csv_path, "r") as f:
            for line in f.readlines():
                values = line.strip().split(",")
                kwargs = {k: v for k, v in zip(model_fields, values)}
                new_cls = model_cls.objects.create(**kwargs)
                data.append(new_cls)
    except Exception as e:
        raise e
    return data
