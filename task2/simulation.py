from math import cos, pi as PI
import numpy as np
import pandas as pd
import time
from modulevariant import fp, Pteor

np.random.seed(int(time.time()))

class Area():                   #класс объекта области обстрела
    def __init__(self, R = 4):
        l = R * cos(PI / 4)
        delta = (1/12)*R
        self.left = (-R-delta, -R-delta)
        self.right = (l + delta, l + delta)

class Dot():                    #класс точки попадания (координаты случайны в пределах Area)
    def __init__(self, left: tuple, right: tuple):
        self.x = np.random.uniform(left[0], right[0])
        self.y = np.random.uniform(left[1], right[1])

def simulate(shots=1000, radius=10) -> tuple:           

    hit = 0
    area = Area(radius) if radius > 0 else Area()
    X, Y = [], []                          #списки координат
    for i in range(shots):  
        M = Dot(area.left, area.right)     #создаем точку
        if fp(M.x, M.y, radius): hit += 1      #подсчет колличества попаданий

        X.append(M.x)                      #добавляем координаты в массивы
        Y.append(M.y)                      #добавляем координаты в массивы

    data = {                               #словарь данных для dataframe
        'J': [i for i in range(1, shots + 1)],
        'X': X,
        'Y': Y,
        'P': [fp(x, y, radius) for x, y in zip(X, Y)] 
    }

    dataframe = pd.DataFrame(data)         #инициализация dataframe pandas
    dataframe.to_csv('./shots.csv', index=False)          #запись в csv
    dataframe.to_excel('./shots.xlsx', index=False)       #запись в excel
    
    return round(hit / shots * 100, 1), Pteor(area, radius) #возвращаем фактическую и теоретическую вероятность



if __name__ == "__main__":                 #точка входа

    shots = int(input("колличество выстрелов: "))        #ввод значений
    radius = int(input("радиус (или 0): "))              #ввод значений

    simulate(shots, radius)                              #запуск симуляции 

    with open('shots.csv', 'r') as file:                  #чтение из csv
        for i in file: print(i)


