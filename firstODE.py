
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def dydx(y,x):
    return x-y

X = np.linspace(0,5,100)
Y_real = X-1+2*np.exp(-X)
Y_pred = np.array(odeint(dydx, 1.0, X))
Y_pred.flatten()

plt.xlabel("Time")
plt.ylabel("Value")
plt.plot(X,Y_pred,X,Y_real,"+")
plt.show()