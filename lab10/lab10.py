import matplotlib.pyplot as plt
import numpy as np
import random


LOWER = -1
UPPER = 0
EPS = 0.003
N = 100000


class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y


def function(x):
    return pow(x,2) + np.sin(x)


def make_plot(l_border, u_border):
    x = []
    a = l_border
    b = u_border
    while a < b:
        x.append(a)
        a+=.00001

    y = [function(x) for x in x]

    plt.figure()
    plt.plot(x,y)
    plt.scatter()
    plt.show()

def half_division(lower_border,upper_border, eps):
    p = 0
    q = 0
    d = .01
    num_of_iteration = 0
    while abs(upper_border - lower_border) > d:
        p = (upper_border + lower_border) / 2.0 + eps

        q = (upper_border + lower_border) / 2.0 - eps

        if function(p) < function(q):
            lower_border = q
        else:
            upper_border = p
        num_of_iteration += 1

    print('Half division method\nNum of iterations = ',num_of_iteration)
    x_cordinate = (upper_border + lower_border)/2.0
    y_cordinate = function(x_cordinate)
    print('x = {0}\ty={1}'.format(x_cordinate, y_cordinate))
    return Point(x_cordinate, y_cordinate)


def random_search(lower_border, upper_border):
    min = 99999
    minx =0
    x = []
    y = []
    num_of_iteration = 0
    for i in range(N):
        x.append(random.uniform(0,1) * (upper_border - lower_border) + lower_border)

    for i in range(N):
        y.append(function(x[i]))

        if min > y[i]:
            min = y[i]
            minx = x[i]

        num_of_iteration+=1
    print('Random Search\nNum of iterations = ', num_of_iteration)
    print('x={0}\t y= {1}'.format(minx, function(minx)))
    return Point(minx, function(minx))

def gradient_method(low_border, eps):
    d = .0001
    x = 1.0
    x0 = 0.7
    h = .1
    num_of_iteration = 0

    while True:
        g = (function(x0+ eps)- function(x0 -eps))/ eps
        i = np.sign(g)
        x = x - h * g
        g = (function(x) - function(x0)) / (x - x0)
        x0 = x
        i1 = np.sign(g)

        if abs(g) < d:
            print('Gradient method\nNum of iterations = ', num_of_iteration)
            print('x={0}\ty={1}'.format(x, function(x)))
            return Point(x, function(x))
        else:
            if i1 != i:
                h /=2.0
            else:
                h*=1.6
            i = i1
        num_of_iteration+=1


def generate_points(lower, upper):
    xlist = []
    while lower <= upper:
        xlist.append(lower)
        lower+=0.01
    ylist = [function(x) for x in xlist]
    return xlist, ylist


def make_plot():
    points_list_x, points_list_y = generate_points(LOWER, UPPER)

    point1 = half_division(LOWER, UPPER, EPS)
    point2 = random_search(LOWER, UPPER)
    point3 = gradient_method(LOWER, EPS)

    plt.figure()
    plt.grid()
    plt.plot(points_list_x, points_list_y)
    plt.scatter(point1.x, point1.y)
    plt.scatter(point2.x, point2.y)
    plt.scatter(point3.x, point3.y)
    plt.show()



if __name__ == '__main__':
    make_plot()

