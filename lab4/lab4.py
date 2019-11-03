from random import random
import matplotlib.pyplot as plt
from math import e

import numpy as np
import xlrd


def function(x):
    if -3 < x <=-2  :
        return 0
    else:
        return pow(e,(-1/(2+x)))


def makeGraphic():
    a, b = -10,10
    x = []
    while a<= b:
        x.append(a)
        a+=.1
    y = [function(i) for i in x]

    plt.subplot()
    plt.plot(x,y)
    plt.title('pow(e,(-1/(2+x)))')
    plt.grid()
    plt.show()


def makeCircleDiagram():
    cityPeople = 90.2
    vilagePeople = 9.8
    labels = 'міські поселення \n\n {0}%'.format(cityPeople), 'сільська місцевість \n\n{0}%'.format(vilagePeople)
    colors = ['gold', 'red']

    sizes = [cityPeople, vilagePeople]

    plt.subplot()
    plt.pie(sizes,  labels=labels, colors=colors)
    plt.show()

'''
def makeBarChart():
    file = 'file.xlsx'
    workbook = xlrd.open_workbook(file)
    first_sheet = workbook.sheet_by_name('Лист1')
    for col in range(first_sheet.ncols):
        x = first_sheet.cell_value(0, col)
        y = first_sheet.cell_value(1, col)

        plt.bar(y, x, align='center')
    plt.show()
'''
def histogram():
    f = open('data.txt')
    data_dict = {}
    for line in f:
        if line.strip():
            key, value = line.split(None, 1)
            data_dict[key] = int(value)
    plt.bar(list(data_dict.keys()), data_dict.values(), color='g')
    plt.grid(True)
    plt.title('')
    plt.show()
    f.close()


histogram()
makeCircleDiagram()
makeGraphic()








