from models.interpretation_func import InterpretationFunc
from utils.helper import check_type
from typing import Set


class Model:
    
    def __init__(self, domain: Set[int], i_func: InterpretationFunc):
        check_type(domain, set, "domain")
        check_type(i_func, InterpretationFunc, "i_func")
        self.domain = domain
        self.i_func = i_func

    def __str__(self):
        return f'{{D={self.domain}; I={self.i_func}}}'

    def __repr__(self):
        return str(self)
