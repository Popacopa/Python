from math import cos, pi

def fp(x: float, y: float, R = 4) -> bool:                      #рассчет попадания
        radius = x**2 + y**2 <= R**2
        a, b = False, False
        l = R * cos(pi / 4)
        a = True if x <= 0 and y <= 0 and radius else False
        b = True if (x <= l and y <= l) and (x >= 0 and y >= 0) else False   
        return b or a


def Pteor(area, radius = 4) -> float:                          #рассчет теоретической вероятности
        X = area.right[0] - area.left[0]
        Y = area.right[1] - area.left[1]
        AreaS = (pi * radius ** 2) / 4
        Pt = AreaS  + (radius * cos(pi / 4)) ** 2
        return round(Pt / (X * Y) * 100, 1)                  #возвращает значение в процентах