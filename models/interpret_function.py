from utils.helper import check_type
from typing import Set


class InterpretFunc:
    
    def __init__(self, true_ps: Set[str]):
        check_type(true_ps, set, "true propositions set")
        self._true_ps = true_ps
    
    def __call__(self, p: str):
        check_type(p, str, "proposition")
        return (p in self._true_ps)
    
    def __str__(self) -> str:
        return str(self._true_ps)
