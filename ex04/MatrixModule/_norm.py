import math

def norm(self):
    return math.sqrt(self.dot(self))

def norm_1(self):
    ret = 0
    for i in self[0]:
        ret += abs(i)
    return ret

def norm_inf(self):
    ret = self[0][0]
    for i in self[0]:
        ret = i if i > ret else ret
    return ret