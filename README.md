# First Order Logic
Model checking functions for First Order Logic, automatically compute, for any closed formula and any model, the truth value of this formula in this model.<br>

# Example of a closed formula
#∃x eat(Sabine,x) ∧ ∃x tall(x) ∧ young(x) <br>
<br> 
exemple = Conjunction(<br>
    Existential(<br>
        PredApp(<br>
            pred=Predicate('eat', 2), args=[Constant(name="Sabine"), Variable(name='x')]<br>
        ), var=Variable(name='x')<br>
    ),<br>
    Existential(<br>
        Conjunction(<br>
            PredApp(<br>
                pred=Predicate('tall', 1), args=[Variable(name='x')]<br>
            ),<br>
            PredApp(<br>
                pred=Predicate('young', 1), args=[Variable(name='x')]<br>
            )<br>
        ),<br>
        var=Variable(name='x')<br>
    )<br>
)<br>

