from models.formula import Formula
from models.fol_model import Model
from models.variable import Variable
from models.variable_assign_func import VarAssignment
from utils.helper import check_type


class Existential(Formula):

    def __init__(self, pred: Formula, var: Variable):
        check_type(pred, Formula, "phi")
        check_type(var, Variable, 'var')
        self._pred = pred
        self._var = var

    def check(self, m, f):
        check_type(m, Model, "m")
        check_type(f, VarAssignment, "f")
        all_check = [self._pred.check(m, f=f.assign(self._var, d)) for d in m.domain]
        return any(all_check)

    def free_variables(self):
        fv = self._pred.free_variables()
        fv.discard(self._var)
        return fv
    
    def __str__(self) -> str:
        return f'(∃{(self._var)} {self._pred})'
