import numpy as np
import matplotlib.pyplot as plt
import os


q0		= 0.
p0		= 1.
omega	= 1.
gamma	= 0.01
T		= 10.
dt		= 0.01
N		= 1000

samples = 1000

sigma = np.sqrt(2 * T * gamma) 

cstep = lambda q, p, xi, thet : dt * dt * 0.5 * (- omega * omega * q - gamma * p) + sigma * np.power(dt, 3/2) * (0.5 * xi + 1/(2*np.sqrt(3)) * thet)
qstep = lambda q, p, xi, thet : q + p * dt + cstep(q,p, xi, thet)
pstep = lambda q1, q2, p, xi, thet : p + dt * 0.5 *(-omega * omega * (q1 + q2)) - dt * gamma * p + sigma * np.sqrt(dt) * xi - gamma * cstep(q1,p,xi,thet)

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
	print(j)

angle = np.arctan2(P, omega * Q)
action = P*P*0.5/omega + omega*Q*Q*0.5

angle = np.transpose(angle)

angle = angle + np.pi

action = np.transpose(action)

#%%
os.system("del \"video\\*.jpg\"")
nframes = 2000000

x = np.asarray([i for i in range(100)])
y = omega/(T)*np.exp(-(x*omega/T))

c = 0

for j in (range(len(angle)) if len(angle) <= nframes else np.linspace(0, len(angle)-1, nframes, dtype=int)):
    # 1
    #plt.subplot(1, 2, 1)
    plt.hist(angle[j], density=True, range=(0, np.pi * 2))
    plt.axhline(y = (1/(np.pi*2)))
    plt.xlim([0, np.pi * 2])
    plt.ylim([0,0.5])
    plt.xlabel("Theta [radianti]")
    plt.ylabel("Densità di probabilità")
    plt.title("t = " + str((j+1) * dt))
    
    # 2
    #plt.subplot(1, 2, 2)
    #plt.hist(action[j], normed=True, range=(0,80))
    #plt.plot(x,y,label="Equilibrio ideale")
    #plt.xlim([0,80])
    #plt.ylim([0,0.125])
    #plt.xlabel("J")
    #plt.ylabel("Densità di probabilità")
    #plt.legend()
    #plt.title("t = " + str((j+1) * dt))
    
    filename = 'foo' + str(c+1).zfill(5) + '.jpg';
    plt.savefig("video\\" + filename)
    plt.clf()
    c += 1
    print(j)

filename = "pendulum_1_omega"
os.system("ffmpeg\\bin\\ffmpeg -y -i \"video\\foo%05d.jpg\" video\\" + filename + ".m4v")

