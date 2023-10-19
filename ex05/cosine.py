from MatrixModule import Vector

def angle_cos(l: Vector, r: Vector):
    if type(l) == type(r) and isinstance(l, Vector) and l.shape == r.shape:
        return (r * l) / (r.norm() * l.norm())
    return