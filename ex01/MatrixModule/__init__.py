from ._class import Matrix, Vector
from ._addition import add, radd, T
from ._division import __rtruediv__, __truediv__
from ._multiplication import mul, rmul
from ._print import __repr__, __str__
from ._substraction import rsub, sub
from ._iterator import it

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
Matrix.T = T