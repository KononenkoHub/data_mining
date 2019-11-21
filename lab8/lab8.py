import matplotlib.pyplot as plt

YEARS = [ 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019 ]
NUMBERS = [ 56035 ,54503, 54437,61711,64693,65369,60414,61404,62939,65616,60745,63352,63139,68325,65152,63975,71595,70509,68793,68994,65782,59860,55627,51720,48159,41929,38283,35268,32872,31665,28244]


def holt_brown_method(alpha, beta,p):
    """
    :param alpha: the smoothing factor
    :param beta: trend smoothing factor
    :param p: the order number of the forecasting period
    :return: list with projected data
    """
    listL = [NUMBERS[0]]
    listT = [0]
    newList = []
    fault = 0

    for i in range(len(NUMBERS)):
        listL.append(alpha * NUMBERS[i] + (1 - alpha) * (listL[i - 1] - listT[i - 1]))
        listT.append(beta * (listL[i] - listL[i - 1]) + (1 - beta) * listT[i - 1])

        newList.append(listL[i] + p*listT[i])

        fault += pow(NUMBERS[i] - newList[i], 2)

    fault = pow(fault, .5)
    print("Fault = {0}".format(fault))

    return newList







if __name__ == '__main__':
    plt.figure()
    plt.plot(YEARS,NUMBERS, label='default')
    plt.plot(YEARS, holt_brown_method(.82, .55,1),color='red', label='alpha = 0.82\nbeta= 0.55')
    plt.plot(YEARS, holt_brown_method(.6, .4,1), color='orange', label='alpha = 0.6\nbeta= 0.4')
    plt.grid()
    plt.legend()
    plt.show()








