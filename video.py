import matplotlib.pyplot as plt
import numpy as np
import os

nframes =200

names = os.listdir("graphics")
    
u = np.load("graphics\\" + "pendulum_1.npy")

c = 0

for j in (range(len(u)) if len(u) <= nframes else np.linspace(0, len(u)-1, nframes, dtype=int)):
    plt.plot(np.linspace(0,10,len(u[j])),u[j],linewidth=2)
    filename = 'foo' + str(c+1).zfill(5) + '.jpg';
    plt.ylim([0,0.4])
    plt.xlabel("x")
    plt.ylabel("u")
    plt.title("t = k * %2.2f"%((j+1)))
    plt.savefig("video\\" + filename)
    plt.clf()
    c += 1
    print(j)

filename = "pendulum_1"
os.system("ffmpeg\\bin\\ffmpeg -y -i \"video\\foo%05d.jpg\" video\\" + filename + ".m4v")
os.system("del \"video\\*.jpg\"")
