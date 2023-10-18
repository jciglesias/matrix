def lerp(l, r, t):
    if type(l) == type(r) and isinstance(t, (float, int)) and t >= 0 and t <= 1:
        if t == 0:
            return l
        return r if t == 1 else (r - l) * t + l
    return