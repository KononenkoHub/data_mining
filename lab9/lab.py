import matplotlib.pyplot as plt
from functions import *

YEARS = [1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005,\
         2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]

NUMBERS = [467047, 466063, 462752, 506099, 536237, 540288, 508266, 498741, 509554, 517726, 487074, 500634, 500700,\
           529027, 523792, 552250, 612604, 588173, 558505, 566371, 521874, 504205, 467277, 440232, 417861, 385717,\
           341200, 321865, 309869, 296758, 272063]


list_of_points = []
for i in range(len(NUMBERS)):
    list_of_points.append(Point(YEARS[i], NUMBERS[i]))

def liner():
    liner_param = findLinerLeastSquareFit(list_of_points)
    liner_param.printArguments()


    yList = []
    for i in range(len(NUMBERS)):
        yList.append(liner_param.x * YEARS[i] + liner_param.y)
    return yList


def square_fit():
    res = findPolynomiaLeastSquareFit(list_of_points)
    print('a = ',res[0],'\nb = ', res[1],'\nc = ', res[2])

    yList2 = []
    for i in range(len(NUMBERS)):
        yList2.append(res[0] * pow(YEARS[i],2) + res[1] * YEARS[i] + res[2])

    return yList2

liner_method_res = liner()
res1 = [float(NUMBERS[-4])] + liner_method_res[-3:]
res2 = [float(NUMBERS[-4])] + square_fit()[-3:]

last_point = Point(YEARS[-2], NUMBERS[-2])


plt.figure()
plt.plot(YEARS[:-3], NUMBERS[:-3])
plt.plot(YEARS, liner_method_res)
plt.plot(YEARS, square_fit())
plt.plot(YEARS[-4:], NUMBERS[-4:])


plt.plot(YEARS[-4:], res1, '-x')
plt.plot(YEARS[-4:], res2, '-o', color='black')

plt.grid()
plt.show()


