from models.interpret_function import InterpretFunc
from models.formula import Formula
from utils.helper import check_type, flatten_list


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
            if isinstance(phi_partial, list) and isinstance(psi_partial, list):
                partial_list = [item2.merge(item1) for item1, item2 in zip(psi_partial, phi_partial) if item2.merge(item1) is not None]
            else:
                res = phi_partial.merge(psi_partial)
                if res is not None:
                    partial_list.append(res)
        
        else:
            if isinstance(phi_partial, list) or isinstance(psi_partial, list):
                partial_list.append(phi_partial)
                partial_list.append(psi_partial)
                partial_list = flatten_list(partial_list)
            else: 
                partial_list = [phi_partial, psi_partial]
        
        return partial_list
    
    def __str__(self) -> str:
        return f"({self._phi} ∧ {self._psi})"
