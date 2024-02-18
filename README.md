# First Order Logic
Model checking functions for First Order Logic, automatically compute, for any closed formula and any model, the truth value of this formula in this model.<br>

## Example of a closed formula
∃x eat(Sabine,x) ∧ ∃x tall(x) ∧ young(x) <br>
<br> 
exemple = Conjunction(<br>
    <td>Existential(<br>
        <td>PredApp(<br>
            <td>pred=Predicate('eat', 2), args=[Constant(name="Sabine"), Variable(name='x')]<br>
        <td>), var=Variable(name='x')<br>
    <td>),<br>
    <td>Existential(<br>
        <td>Conjunction(<br>
            <td>PredApp(<br>
                <td>pred=Predicate('tall', 1), args=[Variable(name='x')]<br>
            <td>),<br>
            <td>PredApp(<br>
                <td>pred=Predicate('young', 1), args=[Variable(name='x')]<br>
            <td>)<br>
        <td>),<br>
        <td>var=Variable(name='x')<br>
    <td>)<br>
)<br>
