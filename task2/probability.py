from simulation import *
from matplotlib import pyplot as plt

if __name__ == "__main__":
    t = [i for i in range(15)]
    Pst = []
    Pt = []
    with open('betaTest.txt', 'w') as file:
        for i in t:
            data = simulate(1000, 4)
            Pst.append(data[0])
            Pt.append(data[1])
            print(data)
            file.write(str(data) + '\n')
    plt.plot(t, Pt)
    plt.scatter(t, Pst, c = 'red', marker = 'o')
    plt.show()