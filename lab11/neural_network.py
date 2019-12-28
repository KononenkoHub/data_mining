import matplotlib.pyplot as plt
import numpy as np
import random
from matplotlib.widgets import Button
from matplotlib.widgets import TextBox


ADITION_POINTS = []
RANDOM_VALUE1= random.randint(0,100)
RANDOM_VALUE2 = random.randint(0,100)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])



class Pair():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_Atributes(self):
        return [self.x, self.y, self.z]


def get_sum(weight_list, x_list):
    summ = 0

    for i in range(len(weight_list)):
        summ+= weight_list[i] * x_list[i]

    return summ

def cross_product(a,b):
    cross = a.x * b.y  -a.y * b.x

    return cross


def length(a):
    d1 = a.x
    d2 = a.y
    return np.sqrt(pow(d1,2) + pow(d2,2))

def line_to_point_distance(a,b,c):
    a_b = Pair(b.x-a.x, b.y-a.y,1)
    a_c = Pair(c.x-a.x, c.y-a.y,1)

    cross = cross_product(a_b,a_c)
    c_d = cross / length(a_b)
    return c_d

def clump(value):
    if value < -1:
        return -1
    elif value> 1:
        return 1
    else:
        return value


def activation_function(summ, alpha):
    return 1.0 / (1.0 + np.exp(-alpha * summ))


def addPoint():
    input_x = input('Enter x = ')
    input_y = input('Enter y = ')
    return input_x, input_y

def function_run():
    global point_y
    cluster_center1 = Pair(-2, 0, 0)
    cluster_center2 = Pair(3, 2, 0)
    cluster_radius = 1.5
    points_number = 10
    eps = .1
    speed_of_learning = .7
    alpha = 1

    max = Pair(0,0,0)
    min = Pair(0,0,0)

    if cluster_center1.x > cluster_center2.x:
        max.x = cluster_center1.x
        min.x = cluster_center2.x
    else:
        max.x = cluster_center2.x
        min.x = cluster_center1.x

    if cluster_center1.y > cluster_center2.y:
        max.y = cluster_center1.y
        min.y = cluster_center2.y
    else:
        max.y = cluster_center2.y
        min.y = cluster_center1.y


    weight_count = 3
    out_of_net = 0
    E = 0 #похибка
    temp = 0
    max_count_of_steps = pow(2,31)
    weight_list = []
    points = []

    mean = 0
    variance = 3


    np.random.seed(RANDOM_VALUE1)
    #points generations
    for i in range(points_number):
        temp_point1 = Pair(np.random.normal(mean, variance) + cluster_center1.x,\
                           np.random.normal(mean, variance) + cluster_center1.y, 1)
        points.append(temp_point1)


        temp_point2 = Pair(np.random.normal(mean, variance) + cluster_center2.x, \
                           np.random.normal(mean, variance) + cluster_center2.y, 1)
        points.append(temp_point2)




    #inizialization weights
    random.seed(RANDOM_VALUE2)
    for i in range(weight_count):
        weight_list.append(random.uniform(0,1))

    #learning
    splitline_y1 = 0
    splitline_y2 = 0
    error = True
    step_counter = 1
    y_value = 0 if (i // 2 == 0) else 1
    stop = False

    list_of_pair = []


    while error:
        if stop: break
        error = False
        for i in range(len(points)):
            out_of_net = activation_function(get_sum(weight_list, points[i].get_Atributes()), alpha)
            E = pow((out_of_net - y_value), 2)



            if E > eps:
                error = True
                for j in range(len(weight_list)):
                    temp = (out_of_net - y_value) * out_of_net * (1 - out_of_net) * points[i].get_Atributes()[j]
                    weight_list[j] -= speed_of_learning * temp

                list_of_pair = []
                splitline_y1 = -((min.x) * weight_list[0] - weight_list[2])/weight_list[1]
                first_line_point = Pair(min.x, splitline_y1,0)
                splitline_y2 = (-(max.x + variance) * weight_list[0] - weight_list[2]) / weight_list[1];
                second_line_point = Pair(max.x , splitline_y2,0)

                list_of_pair.append(first_line_point)
                list_of_pair.append(second_line_point)

        if error:
            step_counter+=1
        if step_counter > max_count_of_steps:
            break
    for i in range(len(points)):
        p = points[i]
        y = (((p.x - min.x)*(splitline_y2 - splitline_y1))/(max.x - min.x)) + splitline_y1
        if p.y > y:
            plt.scatter(points[i].x, points[i].y, color='red')
        else:
            plt.scatter(points[i].x, points[i].y, color='green')


    temp = activation_function(get_sum(weight_list, ADITION_POINTS[len(ADITION_POINTS)-1].get_Atributes()), alpha)


    splitpoint1 = Pair(-10, (((-10 - min.x)*(splitline_y2 - splitline_y1))/(max.x - min.x)) + splitline_y1,0)
    splitpoint2 = Pair(10, (((10 - min.x)*(splitline_y2 - splitline_y1))/(max.x - min.x)) + splitline_y1,0)

    for point in ADITION_POINTS:
        dist = clump(line_to_point_distance(splitpoint1, splitpoint2, point)/5)
        dist = (dist+1)/2
        print(dist)
        if dist < .5:
            plt.scatter(point.x , point.y, color='blue')
        else:
            plt.scatter(point.x, point.y, color='black')

    plt.plot([list_of_pair[0].x, list_of_pair[1].x],[list_of_pair[0].y, list_of_pair[1].y])



    plt.show()


while True:
    x = int(input('Enter x ='))
    y = int(input('Enter y ='))

    input_point = Pair(x, y, 1)
    ADITION_POINTS.append(input_point)
    function_run()






