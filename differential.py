import numpy as np
import matplotlib.pyplot as plt
import os, sys
import matplotlib
import scipy.integrate as integrate
from parameters import *

def a(T, gamma, omega, x, t=0):
    return (T * gamma / omega) * max(0.,x)

def b(gamma, x, t=0):
    return gamma * x

def c(gamma, x=0, t=0):
    return gamma

h = L / M
x = np.linspace(0, L, M + 1)

L = np.zeros((M - 1, M - 1))
R = np.zeros((M - 1, M - 1))
B = np.zeros((M - 1))

for i in range(M - 1):
    L[i, :] = [
        (
            + b(gamma, (i) * h) / (4 * h)
            - a(T, gamma, omega, (i - 1/2) * h) / (2 * h * h)
        ) if j == i - 1 else
        (
            + 1 / (k) 
            - c(gamma) / 2 
            + a(T, gamma, omega, (i + 1/2) * h) / (2 * h * h)
            + a(T, gamma, omega, (i - 1/2) * h) / (2 * h * h)
        ) if j == i else 
        (
            - b(gamma, (i) * h) / (4 * h)
            - a(T, gamma, omega, (i + 1/2) * h) / (2 * h * h)
        ) if j == i + 1 else
        0 for j in range(M - 1)
    ]
    R[i, :] = [
        (
            - b(gamma, (i) * h) / (4 * h)
            + a(T, gamma, omega, (i - 1/2) * h) / (2 * h * h)
        ) if j == i - 1 else
        (
            + 1 / (k) 
            + c(gamma) / 2 
            - a(T, gamma, omega, (i + 1/2) * h) / (2 * h * h)
            - a(T, gamma, omega, (i - 1/2) * h) / (2 * h * h)
        ) if j == i else 
        (
            + b(gamma, (i) * h) / (4 * h)
            + a(T, gamma, omega, (i + 1/2) * h) / (2 * h * h)
        ) if j == i + 1 else
        0 for j in range(M - 1)
    ]
        
# Condizioni iniziali

u = np.empty((nsteps + 1, M + 1))
u[0] = np.asarray([I_0_gaussian(j) for j in x])


#%%
# Calcolo rhs in t=0

bb = R.dot(u[0][1:-1]) + B

for j in range(nsteps):
    print(j)
    # Trova soluzione dentro il dominio
    u[j + 1][1:-1] = np.linalg.solve(L, bb)
    # Aggiorna rhs
    bb = R.dot(u[j + 1][1:-1]) + B

for i in range(len(u)):
    u[i] = u[i] / integrate.simps(u[i], x)

u = np.delete(u, (0), axis=1)

np.save("crank", u)