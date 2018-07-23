import numpy as np
import matplotlib.pyplot as plt

q0		= 0.
p0		= 1.
omega	= 0.5
gamma	= 0.01
T		= 100.
dt		= 0.1
N		= 1000

samples = 100000

qdot = lambda q, p : p
pdot = lambda q, p : - omega * omega * q - gamma * p + np.sqrt(2*T*gamma/dt)*np.random.choice([1.,-1.])

q = np.empty(N)
p = np.empty(N)

q[0] = q0
p[0] = p0

Q = np.empty(samples)
P = np.empty(samples)

for j in range(samples):
	for i in range(1,N):
		# q
		k1 = qdot(q[i-1], p[i-1])
		k2 = qdot(q[i-1] + dt * 0.5 * k1, p[i-1] + dt * 0.5 * k1)
		k3 = qdot(q[i-1] + dt * 0.5 * k2, p[i-1] + dt * 0.5 * k2)
		k4 = qdot(q[i-1] + dt * k3, p[i-1] + dt * k3)

		q[i] = q[i-1] + dt / 6 * (k1 + 2*k2 + 2*k3 + k4)

		# p
		k1 = pdot(q[i-1], p[i-1])
		k2 = pdot(q[i-1] + dt * 0.5 * k1, p[i-1] + dt * 0.5 * k1)
		k3 = pdot(q[i-1] + dt * 0.5 * k2, p[i-1] + dt * 0.5 * k2)
		k4 = pdot(q[i-1] + dt * k3, p[i-1] + dt * k3)

		p[i] = p[i-1] + dt / 6 * (k1 + 2*k2 + 2*k3 + k4)
	Q[j] = q[N-1]
	P[j] = p[N-1]
	print(j)

angle = [np.arctan(omega * Q[i] / P[i]) for i in range(samples)]
action = [P[i]*P[i]*0.5/omega + omega*Q[i]*Q[i]*0.5 for i in range(samples)]


#%%
x = np.asarray([i/10 for i in range(10000)])
y = T/(2*np.pi*omega)*np.exp(-(x*omega/T))

y = y / (np.sum(y)/10)

plt.hist(action, normed = 1)
plt.plot(x,y)
plt.yscale("log")
plt.show()
