import matplotlib.pyplot as plt
from resfile import *

def sumKovzne(n,k):
    summ = 0
    for i in range(k):
        summ+=numOfHumanList[n-i]
    return summ

k = 2
res = []
for j in range(k+1):
    res.append(numOfHumanList[j])

for i in range(1,len(numOfHumanList)):
    value1 = (1.0 /i) * sum(numOfHumanList[:i])
    if i > k:
        value2 = (float(1.0 /k)) * sumKovzne(i,k)
        res.append(value2)







plt.figure()
plt.plot(listOfYear, numOfHumanList, label = 'default')
plt.plot(listOfYear[2:],res[2:])
plt.grid()
plt.legend()
plt.title('Ковзне середнє')
plt.show()