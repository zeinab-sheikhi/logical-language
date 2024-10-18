from models.interpret_function import InterpretFunc
from models.formula import Formula
from ...utils.helper import check_type


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
        phi_partial = self._phi.build(value)
        psi_partial = self._psi.build(value)
        partial_list = []
        
        if value:
            partial_list = [item1.merge(item2) for item1 in psi_partial for item2 in phi_partial if item1.merge(item2) is not None]
        else:
            partial_list = phi_partial + psi_partial
        
        return partial_list
    
    def __str__(self) -> str:
        return f"({self._phi} ∧ {self._psi})"
