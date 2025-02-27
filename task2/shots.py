from math import cos, pi
from loguru import logger
import numpy as np
import pandas as pd
from modulevariant import fp

class Area():
    def __init__(self, R = 4):
        l = R * cos(pi / 4)
        delta = (1/12)*R
        self.left = (-R-delta, -R-delta)
        self.right = (l + delta, l + delta)

class Dot():
    def __init__(self, left: tuple, right: tuple):
        self.x = np.random.uniform(left[0], right[0])
        self.y = np.random.uniform(left[1], right[1])

def main() -> None:

    handler_id = logger.add("file.log") 

    shots = int(input("колличество выстрелов: "))
    radius = int(input("радиус (или 0): "))
    area = Area(radius) if radius > 0 else Area()
    X, Y = [], []
    for i in range(shots):
        M = Dot(area.left, area.right)
        logger.info(f'coords x: {M.x}, y: {M.y}, {fp(M.x, M.y, radius)}')
        X.append(M.x)
        Y.append(M.y)

    data = {
        'J': [i for i in range(1, shots + 1)],
        'X': X,
        'Y': Y,
        'P': [fp(x, y, radius) for x, y in zip(X, Y)] 
    }

if __name__ == "__main__":
    main()
