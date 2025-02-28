from math import cos, pi
from loguru import logger
import numpy as np
import pandas as pd
from modulevariant import fp

class Area():                   #класс объекта области обстрела
    def __init__(self, R = 4):
        l = R * cos(pi / 4)
        delta = (1/12)*R
        self.left = (-R-delta, -R-delta)
        self.right = (l + delta, l + delta)

class Dot():                    #класс точки попадания (координаты случайны в пределах Area)
    def __init__(self, left: tuple, right: tuple):
        self.x = np.random.uniform(left[0], right[0])
        self.y = np.random.uniform(left[1], right[1])

def main() -> None:             #точка входа

    handler_id = logger.add("file.log")     #создаем объект логгера

    shots = int(input("колличество выстрелов: "))
    radius = int(input("радиус (или 0): "))
    area = Area(radius) if radius > 0 else Area()
    X, Y = [], []                          #списки координат
    for i in range(shots):  
        M = Dot(area.left, area.right)     #создаем точку
        logger.info(f'coords x: {M.x}, y: {M.y}, {fp(M.x, M.y, radius)}') #логи
        X.append(M.x)                      #добавляем координаты в массивы
        Y.append(M.y)                      #добавляем координаты в массивы

    data = {                               #словарь данных для dataframe
        'J': [i for i in range(1, shots + 1)],
        'X': X,
        'Y': Y,
        'P': [fp(x, y, radius) for x, y in zip(X, Y)] 
    }

    dataframe = pd.DataFrame(data)         #инициализация dataframe pandas
    dataframe.to_csv('shots.csv', index=False)          #запись в csv
    dataframe.to_excel('shots.xlsx', index=False)       #запись в excel

    with open('data.csv', 'r') as file:                  #чтение из csv
        for i in file: print(i)

    logger.remove(handler_id)
    
if __name__ == "__main__":
    main()

