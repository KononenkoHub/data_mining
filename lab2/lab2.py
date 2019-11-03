import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
from function_module import *



if __name__ == '__main__':
#parametrs and first lists with cordinates
    xmin,xmax = 0,10.0
    dx = .1

    xlist = np.arange(xmin, xmax, dx)
    ylist = [function(x) for x in xlist]
    yWithRandom = [function(x) + random.random() for x in xlist]


#  rows,  cols
    egrid = (10, 10)
    ax = plt.subplot2grid(egrid, (0, 0), colspan=4, rowspan=4)
    ax2 = plt.subplot2grid(egrid, (6, 0), colspan=4, rowspan=4)
    ax3 = plt.subplot2grid(egrid, (0, 5),  colspan=7,rowspan=10)

    ax.grid()
    ax.set_title('sin(0.1*x)*cos(x) ')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')

    ax2.grid()
    ax2.set_title('Update average method')
    ax2.set_xlabel('X')
    ax2.set_ylabel('Y')


    ax3.grid()
    ax3.set_title('Exponential smoothing method')
    ax3.set_xlabel('X')
    ax3.set_ylabel('Y')



# first plot
    ax.plot (xlist, ylist, label = 'default plot') # default plot
    ax.plot (xlist, yWithRandom, label = 'with random', color = 'orange' ) # plot with random
    ax.legend()
#second plot
    ax2.plot (xlist, yWithRandom, label = 'default plot', color = 'orange')  # default plot
    ax2.plot(xlist,updateAverageMetod(yWithRandom),label = 'update average', color = 'green')
    ax2.legend()

#third plot
    ax3.plot(xlist, yWithRandom, color  = 'orange',label = 'default plot') # default plot
    ax3.plot(xlist,ekspo(yWithRandom, 0), color = 'red', label = 'alpha = 0')
    ax3.plot(xlist,ekspo(yWithRandom, .1), color = 'green', label = 'alpha = 0.1')
    ax3.plot(xlist,ekspo(yWithRandom, .4), color = 'blue', label = 'alpha = 0.4')
    ax3.legend()




    mng = plt.get_current_fig_manager()
    mng.window.state('zoomed')
    plt.show()



