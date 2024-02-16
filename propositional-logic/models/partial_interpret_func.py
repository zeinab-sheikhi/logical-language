from utils.helper import check_type


class PartialInterpretfunc:

    def __init__(self, dic):
        check_type(dic, dict, "dict")
        self.dic = dic

    def merge(self, other_func):
        check_type(other_func, PartialInterpretfunc, "other interpreation func")
        dic = dict(self.dic)
        for p, v in other_func.dic.items():
            if (self.dic.get(p, v) != v):
                return None
            dic[p] = v
        return PartialInterpretfunc(dic)

    def __call__(self, p):
        check_type(p, str, "p")
        return self.dic[p]
    
    def __str__(self) -> str:
        return str(self.dic)

    def __repr__(self):
        return str(self)
