from models.formula import Formula
from models.fol_model import Model
from models.variable_assign_func import VarAssignment
from ...utils.helper import check_type


class Negation(Formula):

    def __init__(self, phi: Formula):
        check_type(phi, Formula, "phi") 
        self._phi = phi

    def check(self, m, f):
        check_type(m, Model, "m")
        check_type(f, VarAssignment, "f")
        return not self._phi.check(m, f)
    
    def free_variables(self):
        fv = self._phi.free_variables()
        return fv

    def __str__(self):
        return f'¬{self._phi}'
