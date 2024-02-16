from models.conjunction import Conjunction
from models.interpret_function import InterpretFunc
from models.negation import Negation
from models.partial_interpret_func import PartialInterpretfunc
from models.propositional_letter import PLetter


# print("Interpretation Function")
interp_func = InterpretFunc(true_ps={"p", "r"})
# print("I(p) = ", interp_func("p"))
# print("I(r) = ", interp_func("r"))
# print("I(q) = ", interp_func("q"))
# print("I(s) = ", interp_func("s"))

# print("Propositional Letters")
p_formula = PLetter(proposition="p")
q_formula = PLetter(proposition="q")
r_formula = PLetter(proposition="r")

# print(f"I({str(p_formula)}) = {p_formula.check(interp_func)}")
# print(f"I({str(q_formula)}) = {q_formula.check(interp_func)}")
# print(f"I({str(r_formula)}) = {r_formula.check(interp_func)}")

# print("Negation of a formula")
neg_p_formula = Negation(phi=p_formula)
neg_q_formula = Negation(phi=q_formula)
neg_r_formula = Negation(phi=r_formula)
neg_neg_p_formula = Negation(phi=neg_p_formula)

# print(f"I({str(neg_p_formula)}) = {neg_p_formula.check(interp_func)}")
# print(f"I({str(neg_neg_p_formula)}) = {neg_neg_p_formula.check(interp_func)}")
# print(f"I({str(neg_q_formula)}) = {neg_q_formula.check(interp_func)}")
# print(f"I({str(neg_r_formula)}) = {neg_r_formula.check(interp_func)}")

# print("Conjunction of two formulas")
p_and_q = Conjunction(phi=p_formula, psi=q_formula)
p_and_r = Conjunction(phi=p_formula, psi=r_formula)
q_and_r = Conjunction(phi=q_formula, psi=r_formula)
not_p_and_r = Conjunction(phi=neg_p_formula, psi=r_formula)
not_p_and_q = Conjunction(phi=neg_p_formula, psi=q_formula)
not_q_and_r = Conjunction(phi=neg_q_formula, psi=r_formula)
conj8 = Conjunction(phi=neg_neg_p_formula, psi=p_formula)

# print(f"I{str(conj1)} = {conj1.check(interp_func)}")
# print(f"I{str(conj2)} = {conj2.check(interp_func)}")
# print(f"I{str(conj3)} = {conj3.check(interp_func)}")
# print(f"I{str(conj4)} = {conj4.check(interp_func)}")
# print(f"I{str(conj5)} = {conj5.check(interp_func)}")
# print(f"I{str(conj6)} = {conj6.check(interp_func)}")
# print(f"I{str(conj7)} = {conj7.check(interp_func)}")
# print(f"I{str(conj8)} = {conj8.check(interp_func)}")

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

print("Contradiction")
p_and_not_p = Conjunction(p_formula, neg_p_formula)
print(p_and_not_p)
print(p_and_not_p.build(True))
print(p_and_not_p.build(False))

print("Tautology")
p_or_not_p = Negation(Conjunction(p_formula, neg_p_formula))
print(p_or_not_p)
print(p_or_not_p.build(True))
print(p_or_not_p.build(False))

print("OR")
p_or_q = Negation(Conjunction(phi=neg_p_formula, psi=neg_q_formula))
print(p_or_q)
print(p_or_q.build(False))
print(p_or_q.build(True))
print("Implication")
p_impl_q = Negation(phi=Conjunction(phi=p_formula, psi=neg_q_formula))
print(p_impl_q)
print(p_impl_q.build(False))
print(p_impl_q.build(True))
q_impl_p = Negation(phi=Conjunction(phi=q_formula, psi=neg_p_formula))

print("Biconditional")
p_bicond_q = Conjunction(p_impl_q, q_impl_p)
print(p_bicond_q)
print(p_bicond_q.build(True))
print(p_bicond_q.build(False))
