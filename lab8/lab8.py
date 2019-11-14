import matplotlib.pyplot as plt

years = [ 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019 ]
numbers = [ 56035 ,54503, 54437,61711,64693,65369,60414,61404,62939,65616,60745,63352,63139,68325,65152,63975,71595,70509,68793,68994,65782,59860,55627,51720,48159,41929,38283,35268,32872,31665,28244]








alpha = .82
beta = .6
p = 1

listL = [numbers[0]]
listT = [0]
newList = []
fault=0

for i in range(len(numbers)):
    listL.append(alpha * numbers[i] + (1- alpha) * (listL[i-1] - listT[i-1]))
    listT.append(beta * (listL[i]-listL[i-1]) + (1-beta) * listT[i-1])

    newList.append(listL[i]+listT[i])

    fault+= pow(numbers[i]-newList[i],2)

fault = pow(fault,.5)
print("Fault = {0}".format(fault))



plt.figure()
plt.plot(years, numbers, label='default data')
plt.plot(years[1:],newList[1:])
plt.grid()
plt.legend()
plt.show()

