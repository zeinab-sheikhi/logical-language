def check_type(o, t, name=None):
    if (name is None):
        name = "[no name]"
    assert isinstance(o, t), (f"Type problem: variable {name} (type: {type(o)}; value: {o}) is not an instance of {t}")


def flatten_list(input_list):
    flattened_list = []
    for item in input_list:
        if isinstance(item, list):
            flattened_list.extend(flatten_list(item))
        else:
            flattened_list.append(item)
    return flattened_list
