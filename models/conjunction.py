from models.interpret_function import InterpretFunc
from models.formula import Formula
from utils.helper import check_type


class Conjunction(Formula):
    
    def __init__(self, phi: Formula, psi: Formula):
        check_type(phi, Formula, "phi")
        check_type(psi, Formula, "psi")
        self._phi = phi
        self._psi = psi
    
    def check(self, interp_func: InterpretFunc):
        check_type(interp_func, InterpretFunc, "i_func")
        return self._phi.check(interp_func) and self._psi.check(interp_func)
    
    def build(self):
        pass        

    def __str__(self) -> str:
        return f"({self._phi} ∧ {self._psi})"
