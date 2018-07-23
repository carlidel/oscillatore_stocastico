import numpy as np
import matplotlib.pyplot as plt
import os, sys
import matplotlib

omega	= 1.
gamma	= 0.01
T		= 10

L		= 500.
M		= 1000
k		= 0.1
nsteps	= 30000

x = np.linspace(0,L,M)
x2 = np.linspace(0,L,M*2)

alpha = x2 * (T * gamma / omega)
beta = x * gamma

h = L / (M-1)

A = np.zeros((M-2,M-2))
b = np.zeros((M-2))

for i in range(M-2):
    if i==0:
        A[i,:] = [(-alpha[(i+1)*2 -1]/(2*h*h) -alpha[(i+1)*2 +1]/(2*h*h) + gamma * 0.5)  if j == 0 else (alpha[(i+1)*2 +1]/(2*h*h) + beta[i+1]/(4*h)) + (alpha[(i+1)*2 -1]/(2*h*h) - beta[i+1]/(4*h)) if j == 1 else 0 for j in range(M - 2)]
        b[i] = 0. # Condizione al contorno i=1
    elif i == M - 3:
        A[i,:] = [(alpha[(i+1)*2 -1]/(2*h*h) - beta[i+1]/(4*h)) if j == M - 4 else (-alpha[(i+1)*2 -1]/(2*h*h) -alpha[(i+1)*2 +1]/(2*h*h) + gamma * 0.5) if j == M - 3 else 0 for j in range(M - 2)]
        b[i] = 0. # Condizione al contorno i=M
    else:
        A[i,:] = [(alpha[(i+1)*2 -1]/(2*h*h) - beta[i+1]/(4*h)) if j == i - 1 else (-alpha[(i+1)*2 -1]/(2*h*h) -alpha[(i+1)*2 +1]/(2*h*h) + gamma * 0.5) if j == i else (alpha[(i+1)*2 +1]/(2*h*h) + beta[i+1]/(4*h)) if j == i + 1 else 0 for j in range(M - 2)]

LHS = (np.identity(M-2) / k - A)
RHS = (np.identity(M-2) / k + A)

# Condizioni iniziali

u = np.zeros((nsteps + 1,M))
u[0] = np.asarray([5. if j > 0.9 and j < 1.1 else 0. for j in x])

# Calcolo rhs in t=0

bb = RHS.dot(u[0][1:-1]) + b

for j in range(nsteps):
    print(j)
    # Trova soluzione dentro il dominio
    u[j+1][1:-1] = np.linalg.solve(LHS,bb)
    # Aggiorna rhs
    bb = RHS.dot(u[j+1][1:-1]) + b
    
#%%
os.system("del \"video\\*.jpg\"")

nframes = 1000

names = os.listdir("graphics")
    
c = 0

x_ideal = np.asarray([i for i in range(int(L))])
y_ideal = omega/(T)*np.exp(-(x_ideal*omega/T))


for j in (range(len(u)) if len(u) <= nframes else np.linspace(0, len(u)-1, nframes, dtype=int)):
    plt.plot(np.linspace(0,L,len(u[j])-2),u[j][1:-1],linewidth=0, marker='o', label="Crank-Nicolson")
    plt.plot(x_ideal, y_ideal, linewidth=2, label="Equilibrio ideale")
    plt.legend()
    filename = 'foo' + str(c+1).zfill(5) + '.jpg';
    plt.ylim([0,1])
    plt.xlim([0,40])
    plt.xlabel("J")
    plt.ylabel("Distribuzione di probabilità")
    plt.title("t = " + str((j+1) * k))
    plt.savefig("video\\" + filename)
    plt.clf()
    c += 1
    print(j)

filename = "crank_nicolson_1"
os.system("ffmpeg\\bin\\ffmpeg -y -i \"video\\foo%05d.jpg\" video\\" + filename + ".m4v")
