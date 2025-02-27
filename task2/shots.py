from math import cos, pi
from loguru import logger
import numpy as np
from modulevariant import fp
import matplotlib.pyplot as plt
import matplotlib.patches as patches

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

def set_shots() -> int:
    return int(input("колличество выстрелов: "))

def set_circle() -> int:
    return int(input("радиус (или 0): "))

def main():

    handler_id = logger.add("file.log") 

    #fig, ax = plt.subplots()
    #ax.set_xlim(-10, 10)
    #ax.set_ylim(-10, 10)
    #ax.autoscale()
    #data = np.array([])
    shots = set_shots()
    radius = set_circle()
    area = Area(radius) if radius > 0 else Area()
    #rect = patches.Rectangle(area.left, area.right[0] - area.left[0], area.right[1] - area.left[1], linewidth=2, edgecolor='b', facecolor='none')
    #ax.add_patch(rect)
    for i in range(shots):
        M = Dot(area.left, area.right)
        #plt.scatter(M.x, M.y, color='red')
        logger.info(f'coords x: {M.x}, y: {M.y}, {fp(M.x, M.y, radius)}')
        #plt.draw()
        #plt.pause(0.1)
    plt.show()


if __name__ == "__main__":
    main()