from models.variable import Variable
from ...utils.helper import check_type
from typing import List


class VarAssignment:

    def __init__(self, dic={}):
        check_type(dic, dict, "dic")
        self._dic = dic

    # Returns the variable assignment that only differ from the present one (i.e. `self`) with "x := d".
    # The present assignment is not modified and a new assignment is instantiated.
    def assign(self, x: Variable, d: int):
        check_type(x, Variable, "x")
        check_type(d, int, "d")
        new_dic = {k: v for k, v in self._dic.items()}
        new_dic[x] = d
        return VarAssignment(new_dic)

    # Returns the list obtained from `input` by replacing all variables by their assignments (other elements should appear unaffected).
    # The original list `input` should not be affected.
    def map(self, input: List):
        check_type(input, list, "list")
        tmp = [e for e in input]
        for element in input:
            if isinstance(element, Variable):
                tmp[input.index(element)] = self._dic[element]
        return tmp
    
    def __str__(self):
        return f'{self._dic}'
