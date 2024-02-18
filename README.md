# First Order Logic
Model checking functions for First Order Logic, automatically compute, for any closed formula and any model, the truth value of this formula in this model.<br>

## Example of a closed formula
∃x eat(Sabine,x) ∧ ∃x tall(x) ∧ young(x) <br>

```python
exemple = Conjunction(
    Existential(
        PredApp(
            pred=Predicate('eat', 2), args=[Constant(name="Sabine"), Variable(name='x')]
        ), 
        var=Variable(name='x'),
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


  