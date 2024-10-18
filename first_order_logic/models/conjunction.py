from models.formula import Formula
from models.fol_model import Model
from models.variable_assign_func import VarAssignment
from ...utils.helper import check_type


class Conjunction(Formula):

    def __init__(self, phi: Formula, psi: Formula):
        check_type(psi, Formula, "psi")
        check_type(phi, Formula, "phi")
        self._psi = psi
        self._phi = phi

    def check(self, m: Model, f: VarAssignment):
        check_type(m, Model, "m")
        check_type(f, VarAssignment, "f")
        return self._phi.check(m, f) and self._psi.check(m, f)
    
    def free_variables(self):
        fv = self._psi.free_variables().union(self._phi.free_variables())
        return fv
    
    def __str__(self):
        return f"({self._phi} ∧ {self._psi})"
