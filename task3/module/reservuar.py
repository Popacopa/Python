from abc import ABC, abstractmethod
from math import sqrt
from scipy.optimize import golden
from typing import Tuple
import matplotlib.pyplot as plt

class Reservuar(ABC):

    MATERIALS = {
        "Сталь_XBF": {"плотность": 7850, "цена": 500},
        "Титановый_Сплав_T12": {"плотность": 4500, "цена": 1500},
        "Латунь_113": {"плотность": 8500, "цена": 800},
        "Алюминиевый_Сплав_A231": {"плотность": 2700, "цена": 600},
        "Полимерный_Композит_ПК_421": {"плотность": 1400, "цена": 300}
    }


    def __init__(self, material: str, emkost: float, koeffC: float):
        if material not in self.MATERIALS:
            raise ValueError(f"Неизвестный материал. Доступные: {list(self.MATERIALS.keys())}")
        if not (0.15 <= koeffC <= 0.45):
            raise ValueError("Коэффициент c должен быть в диапазоне 0.15 <= c <= 0.45")
        if emkost <= 0:
            raise ValueError("Объем должен быть положительным")
        
        self.__material = material
        self.__emkost = emkost
        self.__koeffC = koeffC
        self.__rr = 0
        self.__hh = 0
        self.__ff = 0

    def set_hh(self, hh):
        self.__hh = hh

    def set_rr(self, rr):
        self.__rr = rr

    def set_ff(self, ff):
        self.__ff = ff

    @property
    def emkost(self) -> float:
        return self.__emkost
    
    @property
    def parameters(self) -> Tuple[float, float]:
        return self.__rr, self.__hh, self.__ff
    
    @property
    def material(self) -> str:
        return self.__material
    
    @property
    def koeffC(self) -> float:
        return self.__koeffC
    
    @abstractmethod
    def __str__(self): pass
        
    @abstractmethod
    def optimization(self, h): pass




class ReservuarSquareTringe(Reservuar): 

    def __str__(self):
        return (f"Резервуар: {self.__class__.__name__}\n"
                f"Материал: {self.material} {self.MATERIALS[self.material]}\n"
                f"Объем: {self.emkost} м³\n"
                f"Коэффициент c: {self.koeffC}\n"
                f"Текущие параметры:"
                f"  R/H/F: {self.parameters} м\n")
    
    def __surface_area(self,R, c, h) -> float:
        res = (2 * R**2  + R * 1.4 * h * 4) + ((3 * (R * c)**2 * 1.7) / 4 + 3 * h * R * c * 1.7)
        return res
    
    def __FiR(self,V, c, h) -> float:
        if h > 0:
            res = sqrt(V / h * (2 - c**2 / 4))
        else:
            raise ValueError("Радиус(высота) не может быть равен нулю")
        return res
    
    def __FV(self, h) -> float:
        radius = self.__FiR(self.emkost, self.koeffC, h)
        #if radius <= 0: raise ValueError("Радиус(высота) не может быть равен нулю")
        surface_area = self.__surface_area(radius, self.koeffC, h)
        return surface_area
    
    def optimization(self) -> Tuple[float, float, float]:

        def plotter(self) -> None:
            xcoords = []
            ycoords = []
            fig, ax = plt.subplots()
            for i in self.__generator():
                xcoords.append(i[0])
                ycoords.append(i[1])
            ax.plot(xcoords, ycoords)
            ax.plot(xcoords, [min(ycoords) for _ in ycoords], color='red')
            ax.plot([xcoords[ycoords.index(min(ycoords))] for _ in xcoords], ycoords, color='red')
            plt.show()

        plotter(self)
        try:
            res = golden(self.__FV, brack=(0.01, 1000), full_output=True)
        except ValueError:
            raise ValueError("Радиус(высота) не может быть равен нулю")
        Hopt = round(float(res[0]), 2)
        self.set_hh(Hopt)
        Ropt = round(self.__FiR(self.emkost, self.koeffC, self.parameters[1]), 2)
        self.set_rr(Ropt)
        Fopt = round(float(res[1]), 2)
        self.set_ff(Fopt)
        return Hopt, Ropt, Fopt

    def __generator(self, h=1):
        while h < 100:
            f = self.__FV(h)
            h += 0.5
            yield (h, round(f, 2))

    def plotter(self) -> None:
        xcoords = []
        ycoords = []
        fig, ax = plt.subplots()
        for i in self.__generator():
            xcoords.append(i[0])
            ycoords.append(i[1])
        ax.plot(xcoords, ycoords)
        ax.plot(xcoords, [min(ycoords) for _ in ycoords], color='red')
        ax.plot([xcoords[ycoords.index(min(ycoords))] for _ in xcoords], ycoords, color='red')
        plt.show()

        