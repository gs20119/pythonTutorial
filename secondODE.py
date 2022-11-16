
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# second order ode = first order ode with two eqs
# solve [y,y'] vector
def dydx(y,x):
    return [y[1], -2*y[1]-2*y[0]+np.cos(2*x)]

X = np.linspace(0,60,200)
Y_pred = np.array(odeint(dydx,[0,0], X))
print(Y_pred.shape)

plt.xlabel("Time")
plt.ylabel("Value")
plt.plot(X,Y_pred[:,0])
plt.show()