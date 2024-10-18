def check_type(o, t, name=None):
    if (name is None):
        name = "[no name]"
    assert isinstance(o, t), (f"Type problem: variable {name} (type: {type(o)}; value: {o}) is not an instance of {t}")
