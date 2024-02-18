# Propositional Logic
This repository contains Python implementations of the Propositional Logic and First Order Logic.<br>
In Propositional Logic, a model is simply an interpretation function.<br>
An interpretation function is a function that sends each propositional letter to a boolean value.<br>
In this repository, strings are used to represent propositional letters.<br>
To compute which interpretation functions (i.e. models) make true a given formula, we are going to use partial interpretation functions.<br>
We use a partial interpretation function to represent the conditions that are minimally sufficient to make a given formula true (or false). A list of such functions represents a disjunction of conditions. We use such a list to represent the necessary and sufficient conditions to make a given formula true (or false).<br>

List of partial interpretation functions that make (p ∨ ¬q ∨ r) true<br>

```partial = [
    PartialInterpretfunc({"p": True}),
    PartialInterpretfunc({"q": False}),
    PartialInterpretfunc({"r": True})
]```