
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

def pooling(arr):
    m, n = len(arr), len(arr[0])
    ret = np.zeros((m+2, n+2))
    for i in range(m+2):
        for j in range(n+2):
            ret[i,j] = arr[(i-1)%m, (j-1)%n]
    return ret

def next(arr):
    m, n = len(arr), len(arr[0])
    ker = np.array([
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ])
    Arr = pooling(arr)
    count = np.zeros((m,n))
    for i in range(m):
        for j in range(n):
            count[i,j] = np.sum(ker*Arr[i:i+3, j:j+3])
    A = (arr!=0)*(2<=count)*(count<=3)
    B = (arr==0)*(count==3)
    return np.logical_or(A,B)

###########################################################

def init():
    global curr
    IMAGE.set_array(curr)
    return [IMAGE]

def animate(i):
    global curr
    curr = next(curr)
    IMAGE.set_array(curr)
    return [IMAGE]

###########################################################

curr = np.zeros((20, 20))
curr[1,2] = curr[2,3] = curr[3,3] = curr[3,2] = curr[3,1] = 1

FIG = plt.figure()
IMAGE = plt.imshow(curr, cmap='gray')
anim = animation.FuncAnimation(FIG, animate, init_func=init, interval=50, blit=True)
plt.show()

###########################################################