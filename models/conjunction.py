from models.interpret_function import InterpretFunc
from models.formula import Formula
from models.partial_interpret_func import PartialInterpretfunc
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
    
    def build(self, value=True):
        check_type(value, bool, "value")
        if value:
            return [PartialInterpretfunc({f"{self._phi}": value, f"{self._psi}": value})]    
        else:
            return [
                PartialInterpretfunc({f"{self._phi}": value, f"{self._psi}": not value}),
                PartialInterpretfunc({f"{self._phi}": not value, f"{self._psi}": value}),
            ]

    def __str__(self) -> str:
        return f"({self._phi} ∧ {self._psi})"
