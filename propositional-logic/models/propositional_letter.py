from models.interpret_function import InterpretFunc
from models.formula import Formula
from models.partial_interpret_func import PartialInterpretfunc
from ...utils.helper import check_type


class PLetter(Formula):

    def __init__(self, proposition: str):
        check_type(proposition, str, "proposition")
        self._proposition = proposition

    def check(self, interp_func: InterpretFunc):
        check_type(interp_func, InterpretFunc, "i_func")
        return interp_func(self._proposition)

    def build(self, value=True) -> PartialInterpretfunc:
        check_type(value, bool, "value")
        return PartialInterpretfunc({self.__str__(): value})

    def __str__(self) -> str:
        return self._proposition
