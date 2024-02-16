from models.formula import Formula
from models.interpret_function import InterpretFunc
from utils.helper import check_type


class Negation(Formula):
    
    def __init__(self, phi: Formula):
        check_type(phi, Formula, "phi")
        self._phi = phi

    def check(self, interp_func: InterpretFunc):
        check_type(interp_func, InterpretFunc, "i_func")
        return not self._phi.check(interp_func)
    
    def build(self, value=True):
        check_type(value, bool, "value")
        return self._phi.build(value=not value)

    def __str__(self) -> str:
        return f'(¬{self._phi})'
