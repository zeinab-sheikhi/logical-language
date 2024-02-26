from models.constant import Constant
from models.conjunction import Conjunction
from models.interpretation_func import InterpretationFunc
from models.existential import Existential
from models.fol_model import Model
from models.negation import Negation
from models.predicate import Predicate
from models.predicate_app import PredApp
from models.variable_assign_func import VarAssignment
from models.variable import Variable


c_dic = {
    Constant(name="Sabine"): 1,
    Constant(name="Paul"): 2,
    Constant(name="Marie"): 3,
    Constant(name="Marcel"): 4,
    Constant(name="John"): 5,
    Constant(name="Apple"): 6}

p_dic = {
    Predicate("tall", 1): {(1,), (4,)},
    Predicate("young", 1): {(2,), (3,)},
    Predicate("love", 2): {(1, 3), (3, 5), (4, 1)},
    Predicate("eat", 2): {(1, 6)},
    Predicate("like", 2): {(2, 3)}
}

domain = {1, 2, 3, 4, 5, 6}
i_func = InterpretationFunc(c_dic, p_dic)
model = Model(domain, i_func)
f = VarAssignment({Variable(name="x"): 1, Variable(name="y"): 3})

pred = PredApp(pred=Predicate("love", 2), args=[Variable(name="x"), Constant(name="Sabine")])
print(f'{pred} is {pred.check(m=model, f=f)} with f = {f}')
print(f'free variables are: {pred.free_variables()}')

f2 = f.assign(Variable(name='x'), 2)
print(f'{pred} is {pred.check(m=model, f=f2)} with f = {f2}')

f3 = f.assign(Variable(name='x'), 4)
print(f'{pred} is {pred.check(m=model, f=f3)} with f = {f3}')

pred = PredApp(pred=Predicate("love", 2), args=[Constant(name="John"), Variable(name="x")])
f4 = f.assign(Variable(name='x'), 6)
print(f'{pred} is {pred.check(m=model, f=f4)} with f = {f4}')

neg = Negation(PredApp(pred=Predicate("love", 2), args=[Variable(name="x"), Constant(name="Sabine")]))
print(f'{neg} is {neg.check(m=model, f=f)} with f = {f}')
print(f' free variables are: {neg.free_variables()}')

f2 = f.assign(Variable(name='x'), 2)
print(f'{neg} is {neg.check(m=model, f=f2)} with f = {f2}')

f3 = f.assign(Variable(name='x'), 4)
print(f'{neg} is {neg.check(m=model, f=f3)} with f = {f3}')

ex = Existential(
    Existential(PredApp(pred=Predicate("love", 2), args=[Variable(name="x"), Variable(name="y")]), Variable(name='y')),
    Variable(name='x'))

print(f'{ex} is {ex.check(m=model, f=f)}')
print(f'free variables are: {ex.free_variables()}')

ex1 = Existential(Negation(PredApp(pred=Predicate('love', 2), args=[Variable(name='x'), Constant(name="Sabine")])), Variable(name='x'))
print(f"{ex1} is {ex1.check(m=model, f=f)}")
print(f'free variables are: {ex1.free_variables()}')

ex1 = Existential(PredApp(pred=Predicate('love', 2), args=[Constant(name="John"), Variable(name='x')]), Variable(name='x'))
print(f"{ex1} is {ex1.check(m=model, f=f)}")
print(f'free variables are: {ex1.free_variables()}')

exemple = Existential(
    Existential(
        Existential(
            Conjunction(
                PredApp(pred=Predicate("love", 2), args=[Variable(name='x'), Variable(name='y')]),
                PredApp(pred=Predicate("love", 2), args=[Variable(name='z'), Variable(name='x')])),
            var=Variable(name='z')),
        var=Variable(name='y')),
    var=Variable(name='x')) 

print(f"{exemple} is {exemple.check(model, f=f)}")
print(f'free variables are: {exemple.free_variables()}')

exemple = Existential(
    Existential(
        Existential(
            Conjunction(
                PredApp(pred=Predicate("love", 2), args=[Variable(name='y'), Variable(name='x')]),
                PredApp(pred=Predicate("love", 2), args=[Variable(name='z'), Variable(name='x')])),
            var=Variable(name='z')),
        var=Variable(name='y')),
    var=Variable(name='x'))

print(f"{exemple} is {exemple.check(model, f=f)}")


print(f"Domain: {model.domain}")
print(f"Interpret Func: {model.i_func}")

exemple_closed = Existential(
    Existential(
        Existential(
            Conjunction(
                PredApp(pred=Predicate("love", 2), args=[Variable(name='x'), Variable(name='y')]),
                PredApp(pred=Predicate("love", 2), args=[Variable(name='z'), Variable(name='x')])
            ),
            var=Variable(name='z')),
        var=Variable(name='y')),
    var=Variable(name='x'))

print(f"{exemple_closed} is {exemple_closed.check_closed(model)}")

other_closed = Conjunction(
    Existential(
        PredApp(
            pred=Predicate('eat', 2), args=[Constant(name="Sabine"), Variable(name='x')]
        ), var=Variable(name='x')
    ),
    Existential(
        PredApp(
            pred=Predicate('tall', 1), args=[Variable(name='x')]
        ), var=Variable(name='x')
    )
)

print(f"{other_closed} is {other_closed.check_closed(model)}")

other_closed_false = Conjunction(
    Existential(
        PredApp(
            pred=Predicate('eat', 2), args=[Constant(name="Sabine"), Variable(name='x')]
        ), var=Variable(name='x')
    ),
    Existential(
        Conjunction(
            PredApp(
                pred=Predicate('tall', 1), args=[Variable(name='x')]
            ),
            PredApp(
                pred=Predicate('young', 1), args=[Variable(name='x')]
            )
        ),
        var=Variable(name='x')
    )
)

print(f"{other_closed_false} is {other_closed_false.check_closed(model)}")
