from models.constant import Constant
from models.predicate import Predicate
from utils.helper import check_type
from typing import Dict, List


class InterpretationFunc:

    def __init__(self, c_dic: Dict, p_dic: Dict):
        self._c_dic = c_dic
        self._p_dic = p_dic

    def __getitem__(self, x):
        
        if (isinstance(x, Constant)):
            return self._c_dic[x]
        if (isinstance(x, Predicate)):
            return self._p_dic.get(x, set())  # Returns an empty set if the predicate has no entry in `_p_dic`
        raise TypeError
    
    # Returns the list obtained from `input` by replacing all constants by their interpretation (other elements should appear unaffected).
    # The original list `input` should not be affected.
    # input: list of C·s and V·s
    def map(self, input: List):
        check_type(input, list, "l")
        tmp = input
        for index, item in enumerate(input):
            if isinstance(item, Constant):
                tmp[index] = self._c_dic[item]
        return tmp

    def __str__(self):
        tmp = list(self._c_dic.items())
        tmp.extend(self._p_dic.items())
        s = ', '.join([f"{k}: {v}" for (k, v) in tmp])
        return '{' + s + '}'
    
    def __repr__(self):
        return str(self)
