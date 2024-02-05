from models.conjunction import Conjunction
from models.interpret_function import InterpretFunc
from models.negation import Negation
from models.partial_interpret_func import PartialInterpretfunc
from models.propositional_letter import PLetter


# Interpretation function
print("Interpretation Function")
interp_func = InterpretFunc(true_ps={"p", "r"})
print("I(p) = ", interp_func("p"))
print("I(r) = ", interp_func("r"))
print("I(q) = ", interp_func("q"))
print("I(s) = ", interp_func("s"))

# Propositional letters
print("Propositional Letters")
p_formula = PLetter(proposition="p")
q_formula = PLetter(proposition="q")
r_formula = PLetter(proposition="r")

print(f"I({str(p_formula)}) = {p_formula.check(interp_func)}")
print(f"I({str(q_formula)}) = {q_formula.check(interp_func)}")
print(f"I({str(r_formula)}) = {r_formula.check(interp_func)}")

# Negation of a formula
print("Negation of a formula")
neg_p_formula = Negation(phi=p_formula)
neg_q_formula = Negation(phi=q_formula)
neg_r_formula = Negation(phi=r_formula)
neg_neg_p_formula = Negation(phi=neg_p_formula)

print(f"I({str(neg_p_formula)}) = {neg_p_formula.check(interp_func)}")
print(f"I({str(neg_neg_p_formula)}) = {neg_neg_p_formula.check(interp_func)}")
print(f"I({str(neg_q_formula)}) = {neg_q_formula.check(interp_func)}")
print(f"I({str(neg_r_formula)}) = {neg_r_formula.check(interp_func)}")

# Conjunction of two formulas
print("Conjunction of two formulas")
conj1 = Conjunction(phi=p_formula, psi=q_formula)
conj2 = Conjunction(phi=p_formula, psi=r_formula)
conj3 = Conjunction(phi=q_formula, psi=r_formula)
conj4 = Conjunction(phi=neg_p_formula, psi=r_formula)
conj5 = Conjunction(phi=neg_p_formula, psi=q_formula)
conj6 = Conjunction(phi=neg_q_formula, psi=r_formula)
conj7 = Conjunction(phi=neg_p_formula, psi=p_formula)
conj8 = Conjunction(phi=neg_neg_p_formula, psi=p_formula)

print(f"I{str(conj1)} = {conj1.check(interp_func)}")
print(f"I{str(conj2)} = {conj2.check(interp_func)}")
print(f"I{str(conj3)} = {conj3.check(interp_func)}")
print(f"I{str(conj4)} = {conj4.check(interp_func)}")
print(f"I{str(conj5)} = {conj5.check(interp_func)}")
print(f"I{str(conj6)} = {conj6.check(interp_func)}")
print(f"I{str(conj7)} = {conj7.check(interp_func)}")
print(f"I{str(conj8)} = {conj8.check(interp_func)}")

# List of partial interpretation functions that make (p ∨ ¬q ∨ r) true
partial = [
    PartialInterpretfunc({"p": True}),
    PartialInterpretfunc({"q": False}),
    PartialInterpretfunc({"r": True})
]

# List of partial interpretation functions that make (p ∧ ¬q) true
partial1 = [PartialInterpretfunc({"p": True, "q": False})]

print(p_formula.build())
print(q_formula.build())
print(r_formula.build())

print(neg_p_formula.build())
print(neg_q_formula.build(False))
print(neg_neg_p_formula.build())

print(conj7.build())
