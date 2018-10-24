import numpy as np
# Parameters
omega = 1.
gamma = 0.01
T = 10.
dt = 0.2
t_max = 200

omega0 = 1.
omega1 = 2.
# To be multiplied with current time so that it is [0,1]
lambda_par = 1/t_max

dt_2 = dt * dt
dt_3_2 = np.sqrt(np.power(dt, 3))
dt_sqrt = np.sqrt(dt)
omega_2 = omega * omega
sigma = np.sqrt(2 * T * gamma)

# Sampling distribution Langevine
def I_0_gaussian_sampling():
    return np.random.normal(10., 1.)

def theta_0_uniform_sampling():
    return np.random.uniform(0., 2 * np.pi)

def theta_0_peack_sampling():
    return 0.0

def action_angle_to_q_p(I, theta):
    q = np.sqrt(2 * I / omega) * np.sin(theta)
    p = np.sqrt(2 * I * omega) * np.cos(theta)
    return q, p

# Initial distribution Crank
def I_0_gaussian(I):
    return (1 / (np.sqrt(2*np.pi))) * np.exp(-(I-10.)**2 / 2)

# Langevine
N = int(t_max/dt)
samples = 100000
#samples = 1000
q0 = 0.
p0 = 1.

# Crank-Nicolson
L = 200.
M = 4000
#M = 1000
k = dt
nsteps = int(t_max/k)
