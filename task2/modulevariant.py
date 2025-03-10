from math import cos, pi as PI

def fp(x: float, y: float, R = 4) -> bool:                      #рассчет попадания
        radius = x**2 + y**2 <= R**2                          
        a, b = False, False
        l = R * cos(PI / 4)
        a = True if x <= 0 and y <= 0 and radius else False
        b = True if (x <= l and y <= l) and (x >= 0 and y >= 0) else False   
        return b or a


def Pteor(area, radius = 4) -> float:                          #рассчет теоретической вероятности
        X = area.right[0] - area.left[0]                      #получаем длинны ребер Area
        Y = area.right[1] - area.left[1]
        AreaS = (PI * radius ** 2) / 4                        #прощадь сектора круга
        Pt = AreaS  + (radius * cos(PI / 4)) ** 2             #площадь заштрихованной 
        return round(Pt / (X * Y) * 100, 1)                  #возвращает значение в процентах