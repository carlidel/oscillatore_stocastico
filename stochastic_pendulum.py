#!/usr/bin/env python
import numpy as np
import sys

# Parameters

q0		= 0.
p0		= 1.
omega	= 1.
gamma	= 0.01
T		= 10.
dt		= 0.01
N		= 10000
samples = 10000
sigma = np.sqrt(2 * T * gamma) 
omega_2 = omega * omega

# Lambdas

cstep = lambda q, p, xi, thet : dt * dt * 0.5 * (- omega_2 * q - gamma * p) + sigma * np.power(dt, 3/2) * (0.5 * xi + 1/(2*np.sqrt(3)) * thet)
qstep = lambda q, p, xi, thet : q + p * dt + cstep(q,p, xi, thet)
pstep = lambda q1, q2, p, xi, thet : p + dt * 0.5 *(-omega_2 * (q1 + q2)) - dt * gamma * p + sigma * np.sqrt(dt) * xi - gamma * cstep(q1,p,xi,thet)

qa = np.empty(N)
pa = np.empty(N)

qa[0] = q0
pa[0] = p0

Q = np.empty((samples, N))
P = np.empty((samples, N))

for j in range(samples):
	for i in range(1,N):
		xi = np.random.normal()
		thet = np.random.normal()
		# q
		qa[i] = qstep(qa[i-1], pa[i-1], xi, thet)
		# p
		pa[i] = pstep(qa[i-1], qa[i], pa[i-1], xi, thet)
	Q[j] = qa
	P[j] = pa
	#print(j)

angle = np.arctan2(P, omega * Q)
action = P*P*0.5/omega + omega*Q*Q*0.5

angle = np.transpose(angle)

angle = angle + np.pi

action = np.transpose(action)

print("Angle")
np.savetxt(sys.stdout.buffer, angle)
print("Action")
np.savetxt(sys.stdout.buffer, action)
