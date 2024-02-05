from models.interpretation_function import InterpretFunc
from models.propositional_letter import PLetter

# First Instruction
interp_func = InterpretFunc(true_ps={"p", "r"})
print("I(p) = ", interp_func("p"))
print("I(r) = ", interp_func("r"))
print("I(q) = ", interp_func("q"))
print("I(s) = ", interp_func("s"))
print("\n")

# Second Instruction
p_formula = PLetter(proposition="p")
q_formula = PLetter(proposition="q")
r_formula = PLetter(proposition="r")

print(p_formula.check(interp_func))
print(q_formula.check(interp_func))
print(r_formula.check(interp_func))
print("\n")
