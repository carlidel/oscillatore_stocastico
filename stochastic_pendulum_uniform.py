import numpy as np
import pickle
import sys
from parameters import *

# Functions
def cstep(q, p, xi, theta, sigma, dt, dt_2, dt_3_2):
    return (dt_2 * 0.5 * (-omega_2 * q - gamma * p) + sigma * dt_3_2 *
            (0.5 * xi + theta / (2 * np.sqrt(3))) 
			)


def qstep(q, p, xi, theta, sigma, dt, dt_2, dt_3_2):
    return q + p * dt + cstep(q, p, xi, theta, sigma, dt, dt_2, dt_3_2)


def pstep(q1, q2, p, xi, theta, sigma, omega_2, dt, dt_2, dt_3_2, dt_sqrt):
    return (p + dt * 0.5 * (-omega_2 * (q1 + q2)) - dt * gamma * p +
            sigma * dt_sqrt * xi -
            gamma * cstep(q1, p, xi, theta, sigma, dt, dt_2, dt_3_2))


# Initialization
qa = np.empty(N)
pa = np.empty(N)

Q = np.empty((samples, N))
P = np.empty((samples, N))

for j in range(samples):
    I0 = I_0_gaussian_sampling()
    T0 = theta_0_uniform_sampling()
    qa[0], pa[0] = action_angle_to_q_p(I0, T0)
    for i in range(1,N):
        xi = np.random.normal()
        theta = np.random.normal()
        # q
        qa[i] = qstep(qa[i-1], pa[i-1], xi, theta, sigma, dt, dt_2, dt_3_2)
        # p
        pa[i] = pstep(qa[i-1], qa[i], pa[i-1], xi, theta, sigma, omega_2,
                      dt, dt_2, dt_3_2, dt_sqrt)
    Q[j] = qa
    P[j] = pa
    print(str(j) + "/" + str(samples))

angle = np.arctan2(P, omega * Q)
action = P*P*0.5/omega + omega*Q*Q*0.5

angle = np.transpose(angle)
angle = angle + np.pi

action = np.transpose(action)

np.save("action_uniform", action)
np.save("angle_uniform", angle)