from tr import Reservoir


# Параметры материала
material = {
    'thickness': 0.01,  # 1 см
    'density': 7850,    # сталь, кг/м^3
    'price': 50         # руб/кг
}

# Создание резервуара
reservoir = Reservoir(V=10, c=0.4, material=material)

# Оптимизация размеров
R_opt, H_opt = reservoir.optimize()
print(f"Оптимальные параметры: R = {R_opt:.2f} м, H = {H_opt:.2f} м")
print(f"Минимальная площадь поверхности: {reservoir.FF_min:.2f} м²")
print(f"Минимальная стоимость материала: {reservoir.Z_min:.2f} руб")

# Построение графика
reservoir.plot_optimization(h_min=1, h_max=10)