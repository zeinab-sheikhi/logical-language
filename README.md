# Logical Language

This repository contains Python implementations for Propositional Logic and First Order Logic.

# Propositional Logic
This repository contains Python implementations of the Propositional Logic and First Order Logic.<br>
In Propositional Logic, a model is simply an interpretation function.<br>
An interpretation function is a function that sends each propositional letter to a boolean value.<br>
In this repository, strings are used to represent propositional letters.<br>
To compute which interpretation functions (i.e. models) make true a given formula, we are going to use partial interpretation functions.<br>
We use a partial interpretation function to represent the conditions that are minimally sufficient to make a given formula true (or false). A list of such functions represents a disjunction of conditions. We use such a list to represent the necessary and sufficient conditions to make a given formula true (or false).<br>

List of partial interpretation functions that make (p ∨ ¬q ∨ r) true<br>

```python
partial = [
    PartialInterpretfunc({"p": True}),
    PartialInterpretfunc({"q": False}),
    PartialInterpretfunc({"r": True})
]
```

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
```