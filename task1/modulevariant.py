from math import cos, pi as PI

def fp(x: float, y: float, R = 4) -> bool:                      #рассчет попадания
        radius = x**2 + y**2 <= R**2                          
        a, b = False, False
        l = R * cos(PI / 4)
        a = True if x <= 0 and y <= 0 and radius else False
        b = True if (x <= l and y <= l) and (x >= 0 and y >= 0) else False   
        return b or a


def Pteor(surface_area, radius = 4) -> float:                          #рассчет теоретической вероятности
        X = surface_area.right[0] - surface_area.left[0]                      #получаем длинны ребер surface_area
        Y = surface_area.right[1] - surface_area.left[1]
        surface_areaS = (PI * radius ** 2) / 4                        #прощадь сектора круга
        Pt = surface_areaS  + (radius * cos(PI / 4)) ** 2             #площадь заштрихованной 
        return round(Pt / (X * Y) * 100, 1)                  #возвращает значение в процентах