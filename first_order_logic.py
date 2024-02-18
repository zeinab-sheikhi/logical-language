from models.constant import Constant
from models.predicate import Predicate
from models.variable import Variable


sabine = Constant(name="Sabine")
x = Variable(name="x")
eat = Predicate(name="eat", arity=2)

print(isinstance(sabine, Constant))
print(isinstance(x, Variable))
print(isinstance(eat, Predicate))
