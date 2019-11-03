import matplotlib.pyplot as plt
from resfile import *


graph1 =[12435,12576]
graph2 =[12435,12576]
graph3 =[12435,12576]


for i in range(2,len(numOfHumanList)):
    value1 = numOfHumanList[i-1]
    value2 = value1+(value1-numOfHumanList[i-2])
    value3 = value1 * value1/numOfHumanList[i-2]
    graph1.append(value1)
    graph2.append(value2)
    graph3.append(value3)





plt.figure()
plt.plot(listOfYear,numOfHumanList, label = 'default') #def graph
plt.plot(listOfYear[1:],graph1[1:], label = '1')
plt.plot(listOfYear[1:],graph2[1:],label = '2')
plt.plot(listOfYear[1:],graph3[1:],label = '3')
plt.title("'Завтра буде як сьогодні'")
plt.grid()
plt.legend()
plt.show()


