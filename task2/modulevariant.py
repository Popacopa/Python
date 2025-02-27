from math import cos, pi


def fp(x: float, y: float, R = 4) -> bool:
        radius = x**2 + y**2 <= R**2
        a, b = False, False
        l = R * cos(pi / 4)
        a = True if x <= 0 and y <= 0 and radius else False
        b = True if (x <= l and y <= l) and (x >= 0 and y >= 0) else False   
        return b or a


