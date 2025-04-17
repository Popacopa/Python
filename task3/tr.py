import math
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar

class Reservoir:
    def __init__(self, V, c, material):
        """
        Инициализация резервуара
        :param V: объем (м^3)
        :param c: коэффициент c = r/R (отношение радиусов)
        :param material: словарь с параметрами материала {
            'thickness': толщина (м),
            'density': плотность (кг/м^3),
            'price': цена за кг материала
        }
        """
        self.V = V
        self.c = c
        self.material = material
    
    def radius_from_height(self, H):
        """
        Вычисление радиуса R из уравнения объема для заданной высоты H
        Уравнение (5): R = FiR(H)
        """
        # Конкретная реализация зависит от формы резервуара
        # Для цилиндрического резервуара с коническим дном:
        # V = πR²H - (1/3)πr²h_cone, где r = c*R
        # Упрощенный пример (нужно адаптировать под конкретную геометрию):
        return math.sqrt(self.V / (math.pi * H * (1 - self.c**2 / 3)))
    
    def surface_area(self, R, H):
        """
        Вычисление площади поверхности FF
        Уравнение (2)
        """
        # Пример для цилиндрического резервуара с коническим дном:
        r = self.c * R
        # Боковая поверхность цилиндра + боковая поверхность конуса
        return 2 * math.pi * R * H + math.pi * R * math.sqrt(R**2 + H**2)
    
    def cost(self, FF):
        """
        Вычисление стоимости материала
        """
        return self.material['thickness'] * FF * self.material['density'] * self.material['price']
    
    def tabulate(self, h_min, h_max, n_points=100):
        """
        Генератор для табулирования значений площади поверхности
        """
        for i in range(n_points + 1):
            H = h_min + i * (h_max - h_min) / n_points
            R = self.radius_from_height(H)
            FF = self.surface_area(R, H)
            yield (H, FF)

    def optimize(self):
        """
        Оптимизация высоты резервуара для минимальной площади поверхности
        """
        # Функция для оптимизации
        def objective(H):
            R = self.radius_from_height(H)
            return self.surface_area(R, H)
        
        # Начальное приближение
        h0 = math.pow(self.V, 1/3)  # Кубический корень из объема как начальное приближение
        
        # Оптимизация
        result = minimize_scalar(objective, bounds=(0.1, 10*h0), method='bounded')
        
        if not result.success:
            raise ValueError("Оптимизация не удалась")
        
        self.H_opt = result.x
        self.R_opt = self.radius_from_height(self.H_opt)
        self.FF_min = result.fun
        self.Z_min = self.cost(self.FF_min)
        
        return self.R_opt, self.H_opt
    
    def plot_optimization(self, h_min, h_max):
        """
        Построение графика зависимости площади поверхности от высоты
        """
        data = list(self.tabulate(h_min, h_max))
        heights = [d[0] for d in data]
        areas = [d[1] for d in data]
        
        plt.figure(figsize=(10, 6))
        plt.plot(heights, areas, label='Площадь поверхности FF')
        plt.xlabel('Высота H (м)')
        plt.ylabel('Площадь поверхности (м²)')
        plt.title('Зависимость площади поверхности от высоты резервуара')
        
        if hasattr(self, 'H_opt'):
            plt.axvline(self.H_opt, color='r', linestyle='--', 
                       label=f'Оптимальная высота = {self.H_opt:.2f} м')
            plt.axhline(self.FF_min, color='g', linestyle='--', 
                       label=f'Минимальная площадь = {self.FF_min:.2f} м²')
        
        plt.legend()
        plt.grid()
        plt.show()