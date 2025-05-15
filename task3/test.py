from  module import *
from matplotlib import pyplot as plt

a = ReservuarSquareHexagon("Сталь_XBF", 188, 0.45)
b = ReservuarSquareHexagon("Полимерный_Композит_ПК_421", 1000, 0.15)
c = ReservuarSquareHexagon("Латунь_113", 500, 0.25)


with open("results.txt", 'w') as file:
    for i in ReservuarSquareHexagon.items:
        file.write(str(i) + "\n")*2
    file.write("_" * 50 + "\n" * 2)

print("_" * 100 + "\n" * 2)

a.optimization(plot=False)
b.optimization(plot=True)
c.optimization(plot=False)

ReservuarSquareHexagon.items.sort(key=lambda x: x.emkost)

for i in ReservuarSquareHexagon.items:
    print(i)

with open("results.txt", 'a') as file:
    for i in ReservuarSquareHexagon.items:
        file.write(str(i) + "\n")*2


###############################################################


obj1 = ReservuarSquareHexagon("Сталь_XBF", 1000, 0.45)
obj2 = ReservuarSquareHexagon("Сталь_XBF", 1000, 0.35)
obj3 = ReservuarSquareHexagon("Сталь_XBF", 1000, 0.25)
obj4 = ReservuarSquareHexagon("Сталь_XBF", 1000, 0.15)


fig, ax = plt.subplots()
ax.plot(obj1.plotter(plot=False)[0], obj1.plotter(plot=False)[1])
ax.plot(obj2.plotter(plot=False)[0], obj2.plotter(plot=False)[1])
ax.plot(obj3.plotter(plot=False)[0], obj3.plotter(plot=False)[1])
plt.savefig("F(H).png", dpi=300)