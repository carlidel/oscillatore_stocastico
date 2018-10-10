import matplotlib.pyplot as plt
import numpy as np
from parameters import *

def stationary_distribution(action, omega, T):
    return omega / (2 * np.pi * T) * np.exp(- action * omega / T)

#%%

x = np.arange(0., 100., 0.1)
plt.plot(x, stationary_distribution(x, omega, T))
plt.show()
    