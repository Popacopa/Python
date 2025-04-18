from  module import *
from matplotlib import pyplot as plt

a = ReservuarSquareTringe("Сталь_XBF", 188, 0.45)
b = ReservuarSquareTringe("Полимерный_Композит_ПК_421", 1000, 0.35)
c = ReservuarSquareTringe("Латунь_113", 500, 0.25)


with open("results.txt", 'w') as file:
    for i in ReservuarSquareTringe.items:
        file.write(str(i) + "\n")*2
    file.write("_" * 50 + "\n" * 2)

print("_" * 100 + "\n" * 2)

a.optimization(plot=True)
b.optimization(plot=False)
c.optimization(plot=False)

ReservuarSquareTringe.items.sort(key=lambda x: x.emkost)

for i in ReservuarSquareTringe.items:
    print(i)

with open("results.txt", 'a') as file:
    for i in ReservuarSquareTringe.items:
        file.write(str(i) + "\n")*2


###############################################################


obj1 = ReservuarSquareTringe("Сталь_XBF", 1000, 0.45)
obj2 = ReservuarSquareTringe("Сталь_XBF", 1000, 0.35)
obj3 = ReservuarSquareTringe("Сталь_XBF", 1000, 0.25)
obj4 = ReservuarSquareTringe("Сталь_XBF", 1000, 0.15)


fig, ax = plt.subplots()
ax.plot(obj1.plotter(plot=False)[0], obj1.plotter(plot=False)[1])
ax.plot(obj2.plotter(plot=False)[0], obj2.plotter(plot=False)[1])
ax.plot(obj3.plotter(plot=False)[0], obj3.plotter(plot=False)[1])
plt.savefig("F(H).png", dpi=300)