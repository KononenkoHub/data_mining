import math, random

def makeWindow():
    '''this function creating window for input x_max and x_min '''
    def getCordinate():
        res1, res2 = xMin.get(), xMax.get()
        nonlocal cordinateForm
        cordinateForm.quit()
        return res1, res2

    cordinateForm = Tk()
    cordinateForm.geometry('300x200+470+220')
    cordinateForm.title('Сoordinates form')
    cordinateForm.resizable(width=False, height=False)

    xMin = IntVar()
    xMax = IntVar()


    xMinLable = Label(text="x min =")
    xMinLable.place(x=40,y=50)


    xMaxLable = Label(text="x max =")
    xMaxLable.place(x=40, y=100)


    enter1 = Entry(cordinateForm, textvariable = xMin)
    enter1.place(relx=.28, rely=.26)

    enter2 = Entry(cordinateForm, textvariable = xMax)
    enter2.place(relx=.28, rely=.50)

    submitButton = Button(text = 'Start',height = 1, width = 20, command = getCordinate)
    submitButton.place(x=80,y=150)


    cordinateForm.mainloop()

    return getCordinate()

def function(x):
    '''sin(0.1*x) * cos(x)'''
    if x == 0:
        return 0
    else:
        return math.sin(0.1*x) *math.cos(x)


def updateAverageMetod(listOfY):
    '''
    Method
    :param listOfY:
    :return: list with new coordinates - updateAverageY
    '''
    updateAverageY = [listOfY[0]]
    for i in range(1,len(listOfY)):
        updateAverageY.append(updateAverageY[i-1] + ((listOfY[i] - updateAverageY[i-1])/ i))

    return updateAverageY


def ekspo(listOfY,alpha):

    updateAverageY = [listOfY[0]]
    for i in range(1, len(listOfY)):
        updateAverageY.append(updateAverageY[i - 1] + (alpha * (listOfY[i] - updateAverageY[i - 1])))

    return updateAverageY



'''

def kovz(listOfY):
    mylist = listOfY
    N = 20
    cumsum, moving_aves = [0], []

    for i, x in enumerate(mylist, 1):
        cumsum.append(cumsum[i - 1] + x)
        if i >= N:
            moving_ave = (cumsum[i] - cumsum[i - N]) / N
            # can do stuff with moving_ave here
            moving_aves.append(moving_ave)

    return moving_aves+[0]*19
'''