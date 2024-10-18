from ...utils.helper import check_type
from models.fol_model import Model
from models.variable_assign_func import VarAssignment


class Formula:
    # Checks whether the formula is true according to the model `m`.
    # The use of this method requires that the formula be closed.
    # This method does almost nothing by itself. All the work is done by the `check` method defined for each kind of formulas (sub-classes of `Formula`).
    def check_closed(self, m: Model):
        check_type(m, Model, "m")
        f = VarAssignment()
        return self.check(m, f)
    
