from utils.helper import check_type


class Predicate:
    
    def __init__(self, name, arity):
        check_type(name, str, "name")
        check_type(arity, int, "arity")

        self._name = name
        self.arity = arity

    def __eq__(self, other):
        return isinstance(other, Predicate) and (self._name == other._name) and (self.arity == other.arity)

    def __hash__(self):
        return hash((self._name, self.arity))

    def __str__(self):
        return self._name

    def __repr__(self):
        return str(self)
