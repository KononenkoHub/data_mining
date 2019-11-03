import  numpy as np
from my_class import Point
import random


ALPHA = 100


def function(x):
    return 8-2*x


def functionWithRandom(x):
    return function(x) + (random.uniform(0,.5) * ALPHA)


def findLinerLeastSquareFit(points):
    n = len(points)
    Sx = 0
    Sy = 0
    Sxx = 0
    Sxy = 0

    for i in range(0,len(points)):
        pt = points[i]
        Sx += pt.x
        Sy += pt.y
        Sxy +=pt.x * pt.y
        Sxx +=pt.x * pt.x

    m = (n * Sxy - Sx * Sy)/(n * Sxx - Sx * Sx)
    b = (Sy * Sxx - Sxy * Sx)/(n * Sxx - Sx * Sx)
    return Point(m,b)


def findPolynomiaLeastSquareFit(points):
    n = len(points)
    sx4 = 0
    sx3 = 0
    sx2 = 0
    sx = 0
    sx2y = 0
    sy = 0
    sxy = 0

    for i in range(0,n):
        pt = points[i]
        sx4+=pow(pt.x,4)
        sx3+=pow(pt.x,3)
        sx2+=pow(pt.x,2)
        sx +=pt.x
        sy +=pt.y
        sx2y +=pow(pt.x,2)*pt.y
        sxy +=pt.x * pt.y

    matrix1 = [[sx4,sx3,sx2],
               [sx3,sx2,sx],
               [sx2,sx,n]]
    matrix2 = [sx2y,sxy,sy]

    return np.linalg.solve(matrix1,matrix2)
