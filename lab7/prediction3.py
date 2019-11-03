import matplotlib.pyplot as plt
from resfile import *

alpha = .5
lastValue = numOfHumanList[0]
resList1 = [numOfHumanList[0]]



for i in range(1,len(numOfHumanList)):
    value1 = alpha* numOfHumanList[i-1] +(1- alpha)*lastValue
    resList1.append(value1)






plt.figure()
plt.plot(listOfYear, numOfHumanList, label = 'default')
plt.plot(listOfYear[1:], resList1[1:], label = 'alpha = {0}'.format(alpha))
plt.grid()
plt.legend()
plt.title('Експоненціальне середнє')
plt.show()



