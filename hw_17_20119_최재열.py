
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.integrate import odeint

GRAVITY = 9.8
THETA = np.radians(45)
LENGTH = 1.0
RESISTANCE = 0.5
MASS = 1.0

###################################################

# second order ode = first order ode with two eqs
# solve [y,y'] solution, dydx = [y',y'']
def dydx(y,x):
    return [y[1], -(RESISTANCE/MASS)*y[1]-(GRAVITY/LENGTH)*np.sin(y[0])]

X = np.linspace(0,10,200)                            # time t
Y = np.array(odeint(dydx,[THETA,0],X))               # solve theta(t) with odeint
print(Y.shape)

###################################################

fig, axis = plt.subplots()                           # create figure
axis.set(xlim=[-LENGTH-0.5, LENGTH+0.5], ylim=[-LENGTH-0.5, LENGTH+0.5])
axis.set_aspect('equal', adjustable='box')
axis.grid(True, linestyle='--')                      # edit axis settings
line, = axis.plot([], [], color='b', linewidth=2)    # blue line
obj, = axis.plot([], [], 'bo')                       # blue dot object
time_text = axis.text(-LENGTH-0.2, -LENGTH-0.2, "")  # text

###################################################

def init():                                          # init function
    line.set_data([],[])
    return line,

def iter(i):                                         # show objects using theta(t)
    theta = Y[i,0]
    xpos, ypos = LENGTH*np.sin(theta),-LENGTH*np.cos(theta)
    line.set_data([0,xpos],[0,ypos])
    obj.set_data([xpos],[ypos])
    time_text.set_text("time = {:.1f}".format(X[i]))
    return line, obj, time_text

###################################################

anim = animation.FuncAnimation(                      # animate everything
    fig, iter, init_func=init,
    frames=len(X), interval=50, blit=True
)
plt.show()