import numpy as np
import matplotlib.pyplot as plt
import os


q0		= 0.
p0		= 1.
omega	= 1.
gamma	= 0.1
T		= 10.
dt		= 0.1
N		= 1000

samples = 2000

qdot = lambda q, p : p
pdot = lambda q, p : - omega * omega * q - gamma * p + np.sqrt(2*T*gamma/dt)*np.random.choice([1.,-1.])

q = np.empty(N)
p = np.empty(N)

q[0] = q0
p[0] = p0

Q = np.empty((samples, N))
P = np.empty((samples, N))

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
	Q[j] = q
	P[j] = p
	print(j)

angle = np.arctan(omega * Q / P)
action = P*P*0.5/omega + omega*Q*Q*0.5

angle = np.transpose(angle)
action = np.transpose(action)

#%%

nframes = 100

c = 0

for j in (range(len(angle)) if len(angle) <= nframes else np.linspace(0, len(angle)-1, nframes, dtype=int)):
    # 1
    plt.subplot(1, 2, 1)
    plt.hist(angle[j],normed=1.)
    plt.xlim([-np.pi/2,np.pi/2])
    plt.ylim([0,1])
    # 2
    plt.subplot(1, 2, 2)
    plt.xlim([0,10000])
    plt.ylim([0,1])
    plt.hist(action[j], range=(0,100), normed=1.)
    
    filename = 'foo' + str(c+1).zfill(5) + '.jpg';
    plt.savefig("video\\" +      filename)
    plt.clf()
    c += 1
    print(j)

filename = "pendulum_1_omega"
os.system("ffmpeg\\bin\\ffmpeg -y -i \"video\\foo%05d.jpg\" video\\" + filename + ".m4v")
os.system("del \"video\\*.jpg\"")
