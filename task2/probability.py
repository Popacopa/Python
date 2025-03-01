from simulation import *
from matplotlib import pyplot as plt

CICLES = 1000            #колличество итераций

if __name__ == "__main__":
    t = [i for i in range(CICLES)]  #основная ось (временная)
    Pst = []            #массив значений фактической вероятности
    Pt = []             #массив значений теоретической вероятности
    with open("betaTest.txt", 'w') as file:
        for i in t:
            data = simulate(1000, 4)     #запуск симуляции, data = (Pst(i), Pt(i))
            Pst.append(data[0])          #парсинг результатов для построения графиков
            Pt.append(data[1])
            print(data)
            file.write(str(data) + '\n') #запись результатов в файл
    
    plt.plot(t, Pt, color='green')      #инициализация и настройка полотна
    plt.scatter(t, Pst, c = 'red')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("my_plot.png", dpi=300)                  #показать график
    plt.show()