from math import *


C = 0.4

BASE_MATERIAL = {
            'name': 'СтальСталь_ХВГ',
            'htop': 5,   #толщина в мм
            'p': 12000,   #плотность в кг/м3
            'price': 1000, #цена за кг
        }

FIGURES = {                     #фигуры
            1: ("Окружность", 3.14, ...),
            2: ("Треугольник", 0.75, ...),          # коэффициент 'x' таков, что S = x * R^2
            3: ("Квадрат", 2, ...),                 
            4: ("Пятиугольник", 2.38, ...),
            5: ("Шестиугольник", 2.55, ...),
        }

class Reservoir:
    def __init__(self, figs: tuple, material: dict, V: float, C = C):
        self.V = V
        self.C = C
        try:
            self.big, self.small = figs
        except ValueError or TypeError or KeyError:
            self.big = self.small = 1    #по умолчанию окружность
        try:
            self.material = material
        except ValueError or TypeError or KeyError:
            self.material = BASE_MATERIAL   #по умолчанию сталь


    def radius(self, H:float) -> float:
            R = sqrt(self.V / (FIGURES[self.big][1] - \
                               FIGURES[self.small][1] * self.C**2) * H)
            return R
    
    def surface_area(self, R:float, H:float) -> float:
        r = self.C * R
        s = FIGURES[self.big][1] * R**2 - FIGURES[self.small][1] * r**2

    """ def surface_area(self, R:float, H:float) -> float:
        match self.big:
            case 1:
                return self.V / H + 2 * PI * R * H + 2 * PI * R * self.C * H """
        

t = Reservoir((2, 2), BASE_MATERIAL, V=1000)

print(f'{t.radius(10):.2f}')


