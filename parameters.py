import numpy as np
# Parameters
omega = 1.
gamma = 0.01
T = 10.
dt = 0.1
t_max = 10

omega0 = 1.
omega1 = 2.
# To be multiplied with current time so that it is [0,1]
lambda_par = 1/t_max

dt_2 = dt * dt
dt_3_2 = np.power(dt, 3 / 2)
dt_sqrt = np.sqrt(dt)
omega_2 = omega * omega
sigma = np.sqrt(2 * T * gamma)

# Liouville
N = int(dt/t_max)
samples = 10
q0 = 0.
p0 = 1.

# Crank-Nicolson
L = 500.
M = 1000
k = dt
nsteps = int(k/t_max)
