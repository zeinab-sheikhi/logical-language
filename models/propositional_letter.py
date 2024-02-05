from models.interpretation_function import InterpretFunc
from models.formula import Formula
from utils.helper import check_type


class PLetter(Formula):

    def __init__(self, proposition: str):
        check_type(proposition, str, "proposition")
        self._proposition = proposition

    def check(self, interp_func: InterpretFunc):
        check_type(interp_func, InterpretFunc, "interpretation function")
        return interp_func(self._proposition)

    def build(self, value=True) -> list:
        pass

    def __str__(self) -> str:
        return self._proposition
