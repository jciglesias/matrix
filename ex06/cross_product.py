from MatrixModule import Vector

def cross_product(l: Vector, r: Vector):
    if type(l) == type(r) and isinstance(l, Vector) and l.shape == r.shape:
        ret = []
        for j in range(l.shape[1]):
            if (j + 2) < l.shape[1]:
                ret.append(l[0][j+1] * r[0][j+2] - l[0][j+2] * r[0][j+1])
            elif (j + 1) == l.shape[1] - 1:
                ret.append(l[0][j + 1] * r[0][0] - l[0][0] * r[0][j + 1])
            else:
                ret.append(l[0][0] * r[0][j - 1] - l[0][j - 1] * r[0][0])
        return Vector([ret])
    return