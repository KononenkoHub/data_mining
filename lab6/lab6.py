import math
import matplotlib.pyplot as plt
import numpy as np
import random


MEAN = 0
VARIANCE = 1
T = 3


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Cluster():
    def __init__(self, points):
        self.points = points


def distance(point1, point2):
    return math.sqrt(pow((point2.x-point1.x), 2)) + pow(point2.y-point1.y, 2)


def generate_all_points(centers, mean, variance):
    generate_list = []
    for center_point in range(len(centers)):
        for i in range(33):
            generate_list.append(Point(np.random.normal(mean, variance)+center_point_list[center_point].x,\
                                       np.random.normal(mean, variance)+center_point_list[center_point].y))
    return generate_list


def clusterizate(generate_list):
    cluster_list = []
    for i in range(len(generate_list)):
        current_point = generate_list[i]
        min_value = 20000
        index = -1

        for j in range(len(cluster_list)):
            current_distance = distance(current_point, cluster_list[j].points[0])
            if current_distance < T:
                if current_distance < min_value:
                    min_value = current_distance
                    index = j

        if index >= 0:
            cluster_list[index].points.append(current_point)

        elif index < 0:
            cluster_list.append(Cluster([]))
            temp = cluster_list[len(cluster_list)-1]
            temp.points.append(current_point)

    return cluster_list


if __name__ == '__main__':
    center_point_list = [Point(7, 3), Point(9, -1), Point(6, 6), Point(-4, 9)]

    all_points = generate_all_points(center_point_list, MEAN, VARIANCE)

    clusters = clusterizate(all_points)

    colors = ["#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)])
              for i in range(len(clusters))]

    plt.figure()
    plt.title('Вхідні дані')
    plt.grid()
    plt.axvline(0)
    plt.axhline(0)
    for point in all_points:
        plt.scatter(point.x, point.y, color='red')

    plt.figure()
    plt.title('Кластери')
    plt.grid()
    plt.axvline(0)
    plt.axhline(0)

    for i in range(len(clusters)):
        clusters[i].color = colors[i]
        for point in clusters[i].points:
            plt.scatter(point.x, point.y, color=clusters[i].color)

    print("Num of clusters = ", len(clusters))

    plt.show()
