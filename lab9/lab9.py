import math
from random import gauss
import matplotlib.pyplot as plt

MEAN = 0
VARIANCE = 2




class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y


class Cluster():
    def __init__(self,points,threshold,color):
        self.points = points
        self.threshold = threshold
        self.color = color



def distance(Point1,Point2):
    return math.sqrt(pow((Point2.x-Point1.x),2)) + pow(Point2.y-Point1.y,2)



center_poin_list = [Point(7,3),Point(9,-1),Point(6,6),Point(-4,9)]
all_points = []
cluster_list = [Cluster([],5,'blue'),Cluster([],5,'red'),Cluster([],5,'green'),Cluster([],5,'orange')]






for point in range(len(center_poin_list)):
    for i in range(33):
        all_points.append(Point(gauss(MEAN, math.sqrt(VARIANCE))+center_poin_list[point].x,\
                                            gauss(MEAN, math.sqrt(VARIANCE))+center_poin_list[point].y))




for i in range(len(all_points)):
    current_point = all_points[i]
    min_value = 200000000
    index = -1
    for j in range(len(cluster_list)):
        current_distance = distance(current_point,center_poin_list[j])
        if current_distance < cluster_list[j].threshold:
            if current_distance < min_value:
                min_value = current_distance
                index = j
    if index >= 0:
        cluster_list[index].points.append(current_point)






'''input data plot'''
plt.figure()
plt.title('Вхідні дані')
plt.grid()
plt.axvline(0)
plt.axhline(0)

for point in all_points:
    plt.scatter(point.x,point.y, color='red')

'''result data plot'''
plt.figure()
plt.title('Кластери')
plt.grid()
plt.axvline(0)
plt.axhline(0)

for cluster in cluster_list:
    for point in cluster.points:
        plt.scatter(point.x,point.y,color=cluster.color)

for center_point in center_poin_list:
    plt.scatter(center_point.x,center_point.y, color='black', marker='s', s=50)

plt.show()
