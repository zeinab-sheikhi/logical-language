from models.formula import Formula
from models.fol_model import Model
from models.predicate import Predicate
from models.variable import Variable
from models.variable_assign_func import VarAssignment
from typing import List
from utils.helper import check_type


class PredApp(Formula):
    
    def __init__(self, pred: Predicate, args: List):
        check_type(pred, Predicate, "pred")
        assert (pred.arity == len(args)), f"{pred.arity} argument·s expected but {len(args)} given."
        check_type(args, list, "args")
        self._pred = pred
        self._args = args

    # Checks whether the formula is true according to the model `m` and the variable assignment `f`.
    def check(self, m: Model, f: VarAssignment):
        check_type(m, Model, "m")
        check_type(f, VarAssignment, "f")
        pred_interpret = m.i_func[self._pred]

        # map each variable to its corresponding value assigned by assignment function
        var_mapped = f.map(self._args)	
        # map each constant to its corresponding individual assigned by interpretation function
        const_mapped = m.i_func.map(var_mapped)
        # convert the resulting list to tuple because in interpretation of predicates we have list of tuples
        arg_tuple = tuple(const_mapped)

        if arg_tuple in pred_interpret:
            return True
        else:
            return False
    
    def free_variables(self):
        fv = [item for item in self._args if isinstance(item, Variable)]
        return set(fv)
    
    def __str__(self):
        return f"{self._pred}({','.join([str(x) for x in self._args])})"
