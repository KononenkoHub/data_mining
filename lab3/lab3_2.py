import matplotlib.pyplot as plt
import numpy as np
from functions import *


if __name__ == "__main__":
    x = []
    a,b = -5,5
    while a <= b:
        x.append(a)
        a += .1


    y = [function(i) for i in x]
    yWithRandom = [functionWithRandom(i) for i in x]

    listOfPoints = []

    for i in range(len(x)):
        listOfPoints.append(Point(x[i], yWithRandom[i]))



    linerParam = findLinerLeastSquareFit(listOfPoints)

    yList = []
    for i in range(len(x)):
        yList.append(linerParam.x * x[i] + linerParam.y)


    res = findPolynomiaLeastSquareFit(listOfPoints)

    yList2 = []
    for i in range(len(x)):
        yList2.append(res[0] * pow(x[i],2) + res[1] * x[i] + res[2])


    plt.figure()
    plt.plot(x,y, label = 'Початковий графік')
    plt.plot(x,yWithRandom, label = 'Графік з шумами')
    plt.plot(x,yList, label = 'Лінійна емпірична')
    plt.plot(x,yList2, label = 'Лінійна квадратична')
    plt.legend()
    plt.grid()
    plt.show()

