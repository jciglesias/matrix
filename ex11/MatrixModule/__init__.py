from ._class import Matrix, Vector
from ._addition import add, radd, T, iadd
from ._division import __rtruediv__, __truediv__
from ._multiplication import mul, rmul, determinant
from ._print import __repr__, __str__
from ._substraction import rsub, sub
from ._iterator import it, getitm
from ._norm import norm, norm_1, norm_inf
from ._trace import trace
from ._row_echelon import row_echelon

Matrix.__add__ = add
Matrix.__mul__ = mul
Matrix.__radd__ = radd
Matrix.__sub__ = sub
Matrix.__rsub__ = rsub
Matrix.__truediv__ = __truediv__
Matrix.__rtruediv__ = __rtruediv__
Matrix.__rmul__ = rmul
Matrix.__str__ = __str__
Matrix.__repr__ = __repr__
Matrix.__iter__ = it
Matrix.__getitem__ = getitm
Matrix.__iadd__ = iadd
Matrix.T = T
Matrix.trace = trace
Matrix.row_echelon = row_echelon
Matrix.determinant = determinant
Vector.norm = norm
Vector.norm_1 = norm_1
Vector.norm_inf = norm_inf