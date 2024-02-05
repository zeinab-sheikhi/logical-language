# Checks that `o` is an instance of `t` (ex: integer, list). Produces a clear error message otherwise.
# This function is not essential but can help a lot for debugging.
def check_type(o, t, name=None):
    if (name is None):
        name = "[no name]"
    assert isinstance(o, t), (f"Type problem: variable {name} (type: {type(o)}; value: {o}) is not an instance of {t}")
