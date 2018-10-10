import numpy as np
import pickle
import sys
from parameters import *


# Functions
def cstep(q, p, xi, theta, dt_2, dt_3_2):
    return (dt_2 * 0.5 * (-omega_2 * q - gamma * p) +
            sigma * dt_3_2 * (0.5 * xi + theta / (2 * np.sqrt(3))))


def qstep(q, p, xi, theta, dt, dt_2, dt_3_2):
    return q + p * dt + cstep(q, p, xi, theta, dt_2, dt_3_2)


def pstep(q1, q2, p, xi, theta, omega_2, dt, dt_2, dt_3_2, dt_sqrt):
    return (
        p + dt * 0.5 * (-omega_2 * (q1 + q2)) - dt * gamma * p +
        sigma * dt_sqrt * xi - gamma * cstep(q1, p, xi, theta, dt - 2, dt_3_2))


# Initialization
qa = np.empty(N)
pa = np.empty(N)

qa[0] = q0
pa[0] = p0

Q = np.empty((samples, N))
P = np.empty((samples, N))

for j in range(samples):
    for i in range(1, N):
        xi = np.random.normal()
        theta = np.random.normal()
        omega = (i * dt * lambda_par * omega1 
                 + (1 - i * dt * lambda_par) * omega0)
        omega_2 = omega * omega
        # q
        qa[i] = qstep(qa[i - 1], pa[i - 1], xi, theta, dt, dt_2, dt_3_2)
        # p
        pa[i] = pstep(qa[i - 1], qa[i], pa[i - 1], xi, theta, omega_2, dt,
                      dt_2, dt_3_2, dt_sqrt)
    Q[j] = qa
    P[j] = pa
    print(str(j) + "/" + str(samples))

angle = np.arctan2(P, omega * Q)
action = P * P * 0.5 / omega + omega * Q * Q * 0.5

angle = np.transpose(angle)
angle = angle + np.pi

action = np.transpose(action)

np.save("action", action)
np.save("angle", angle)