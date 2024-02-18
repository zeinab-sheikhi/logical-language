from utils.helper import check_type


class Variable:
    
    def __init__(self, name):
        check_type(name, str, "name")
        self._name = name

    def __eq__(self, other):
        return isinstance(other, Variable) and self._name == other._name

    def __hash__(self):
        return hash(self._name)

    def __str__(self):
        return self._name

    def __repr__(self):
        return str(self)
