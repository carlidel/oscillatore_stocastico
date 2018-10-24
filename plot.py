import matplotlib.pyplot as plt
import numpy as np
import os
from parameters import *

dpi = 300
tskip = 1
p = 0

def stationary_distribution(action, omega, T):
    return omega / (T) * np.exp(- action * omega / T)

#%%
# Make dirs
os.system("mkdir langevine")
os.system("mkdir langevine_time")
os.system("mkdir langevine_uniform")
os.system("mkdir langevine_time_uniform")
os.system("mkdir crank")
os.system("mkdir crank_time")
os.system("mkdir crank_uniform")
os.system("mkdir crank_time_uniform")

#%%
# Stationary Distribution

x = np.arange(0., 100., 0.1)
plt.plot(x, stationary_distribution(x, omega, T))
#plt.show()

#%%

# Langevine
os.system("del \"langevine\\*.jpg\"")

action = np.load("action.npy")
angle = np.load("angle.npy")

action_max = np.amax(action)
p = 0
for i in range(len(action)):
    if i % tskip == 0:
        print(str(i) + "/" + str(len(action)))
        # Action
        plt.subplot(121)
        plt.hist(action[i], range=(0, action_max), bins = 100, density=True)
        plt.plot(x, stationary_distribution(x, omega, T), label="Equilibrium")
        plt.xlabel("I")
        plt.ylabel("Probability distribution")
        plt.title("Action Variable, t = {:.2f}".format(i * dt))
        # Angle
        plt.subplot(122)
        plt.hist(angle[i], range=(0, 2 * np.pi), bins = 100, density=True)
        plt.xlabel("Theta")
        plt.ylabel("Probability distribution")
        plt.title("Angle Variable, t = {:.2f}".format(i * dt))
        # Save
        plt.tight_layout()
        plt.savefig("langevine/foo" + str(p).zfill(5) + ".jpg", dpi=dpi)
        plt.clf()
        p += 1

# Make video
filename = "langevine"
os.system("ffmpeg -y -i \"langevine\\foo%05d.jpg\" " + filename + ".mp4")

#%%
# Langevine Uniform
os.system("del \"langevine_uniform\\*.jpg\"")

action = np.load("action_uniform.npy")
angle = np.load("angle_uniform.npy")

action_max = np.amax(action)
p = 0
for i in range(len(action)):
    if i % tskip == 0:
        print(str(i) + "/" + str(len(action)))
        # Action
        plt.subplot(121)
        plt.hist(action[i], range=(0, action_max), bins = 100, density=True)
        plt.plot(x, stationary_distribution(x, omega, T), label="Equilibrium")
        plt.xlabel("I")
        plt.ylabel("Probability distribution")
        plt.title("Action Variable, t = {:.2f}".format(i * dt))
        # Angle
        plt.subplot(122)
        plt.hist(angle[i], range=(0, 2 * np.pi), bins = 100, density=True)
        plt.xlabel("Theta")
        plt.ylabel("Probability distribution")
        plt.title("Angle Variable, t = {:.2f}".format(i * dt))
        # Save
        plt.tight_layout()
        plt.savefig("langevine_uniform/foo" + str(p).zfill(5) + ".jpg", dpi=dpi)
        plt.clf()
        p += 1

# Make video
filename = "langevine_uniform"
os.system("ffmpeg -y -i \"langevine_uniform\\foo%05d.jpg\" " + filename + ".mp4")

#%%
# Crank-Nicolson
os.system("del \"crank\\*.jpg\"")
u = np.load("crank.npy")
x = np.linspace(0, L, M)
action = np.load("action.npy")
p = 0
for i in range(len(action)):
    if i % tskip == 0:
        print(str(i) + "/" + str(len(u)))
        plt.hist(action[i], bins = 100, range=(0, 100), density=True)
        plt.xlim(0, 100)
        plt.plot(x, u[i], label="Crank-Nicolson")
        plt.plot(x, stationary_distribution(x, omega, T), label="Equilibrium")
        plt.xlabel("I")
        plt.ylabel("Probability distribution")
        plt.title("Action Variable, t = {:.2f}".format(i * dt))
        plt.legend()
        # Save
        plt.tight_layout()
        plt.savefig("crank/foo" + str(p).zfill(5) + ".jpg", dpi=dpi)
        plt.clf()
        p += 1

# Make video
filename = "crank"
os.system("ffmpeg -y -i \"crank\\foo%05d.jpg\" " + filename + ".mp4")

#%%
# Crank-Nicolson_uniform
os.system("del \"crank_uniform\\*.jpg\"")

u = np.load("crank.npy")
x = np.linspace(0, L, M)
action = np.load("action_uniform.npy")
p = 0
for i in range(len(action)):
    if i % tskip == 0:
        print(str(i) + "/" + str(len(action)))
        plt.hist(action[i], range=(0, 100), bins = 100, density=True)
        plt.xlim(0, 100)
        plt.plot(x, u[i], label="Crank-Nicolson")
        plt.plot(x, stationary_distribution(x, omega, T), label="Equilibrium")
        plt.xlabel("I")
        plt.ylabel("Probability distribution")
        plt.title("Action Variable, t = {:.2f}".format(i * dt))
        plt.legend()
        # Save
        plt.tight_layout()
        plt.savefig("crank_uniform/foo" + str(p).zfill(5) + ".jpg", dpi=dpi)
        plt.clf()
        p += 1

# Make video
filename = "crank_uniform"
os.system("ffmpeg -y -i \"crank_uniform\\foo%05d.jpg\" " + filename + ".mp4")

""" #%%
# Langevine_time
os.system("del \"langevine_time\\*.jpg\"")

action = np.load("action_time.npy")
angle = np.load("angle_time.npy")

action_max = np.amax(action)
for i in range(len(action)):
    if i % tskip == 0:
        print(str(i) + "/" + str(len(action)))
        # Action
        plt.subplot(121)
        plt.hist(action[i], range=(0, action_max), bins=100, density=True)
        plt.xlabel("I")
        plt.ylabel("Probability distribution")
        plt.title("Action Variable, t = {:.2f}".format(i * dt))
        # Angle
        plt.subplot(122)
        plt.hist(angle[i], range=(0, 2 * np.pi), bins=100, density=True)
        plt.xlabel("Theta")
        plt.ylabel("Probability distribution")
        plt.title("Angle Variable, t = {:.2f}".format(i * dt))
        # Save
        plt.tight_layout()
        plt.savefig("langevine_time/foo" + str(i).zfill(5) + ".jpg", dpi=dpi)
        plt.clf()

# Make video
filename = "langevine_time"
os.system("ffmpeg -y -i \"langevine_time\\foo%05d.jpg\" " + filename + ".m4v")

#%%
# Langevine_time_uniform
os.system("del \"langevine_time_uniform\\*.jpg\"")

action = np.load("action_time_uniform.npy")
angle = np.load("angle_time_uniform.npy")

action_max = np.amax(action)
for i in range(len(action)):
    if i % tskip == 0:
        print(str(i) + "/" + str(len(action)))
        # Action
        plt.subplot(121)
        plt.hist(action[i], range=(0, action_max), bins=100, density=True)
        plt.xlabel("I")
        plt.ylabel("Probability distribution")
        plt.title("Action Variable, t = {:.2f}".format(i * dt))
        # Angle
        plt.subplot(122)
        plt.hist(angle[i], range=(0, 2 * np.pi), bins=100, density=True)
        plt.xlabel("Theta")
        plt.ylabel("Probability distribution")
        plt.title("Angle Variable, t = {:.2f}".format(i * dt))
        # Save
        plt.tight_layout()
        plt.savefig(
            "langevine_time_uniform/foo" + str(i).zfill(5) + ".jpg", dpi=dpi)
        plt.clf()

# Make video
filename = "langevine_time_uniform"
os.system("ffmpeg -y -i \"langevine_time_uniform\\foo%05d.jpg\" " + filename +
          ".m4v")


#%%
# Crank-Nicolson-Time
os.system("del \"crank_time\\*.jpg\"")

u = np.load("crank_time.npy")
x = np.linspace(0, L, M)
action = np.load("action_time.npy")
for i in range(len(action)):
    if i % tskip == 0:
        print(str(i) + "/" + str(len(action)))
        plt.hist(action[i], range=(0, 100), bins=100, density=True)
        plt.xlim(0, 100)
        plt.plot(x, u[i], label="Crank-Nicolson")
        plt.plot(x, stationary_distribution(x, omega, T), label="Equilibrium")
        plt.xlabel("I")
        plt.ylabel("Probability distribution")
        plt.title("Action Variable, t = {:.2f}".format(i * dt))
        plt.legend()
        # Save
        plt.tight_layout()
        plt.savefig("crank_time/foo" + str(i).zfill(5) + ".jpg", dpi=dpi)
        plt.clf()

# Make video
filename = "crank_time"
os.system("ffmpeg -y -i \"crank_time\\foo%05d.jpg\" " + filename + ".m4v")


#%%
# Crank-Nicolson-Time_uniform
os.system("del \"crank_time_uniform\\*.jpg\"")

u = np.load("crank_time.npy")
x = np.linspace(0, L, M)
action = np.load("action_time_uniform.npy")
for i in range(len(action)):
    if i % tskip == 0:
        print(str(i) + "/" + str(len(action)))
        plt.hist(action[i], range=(0, 100), bins = 100, density=True)
        plt.xlim(0, 100)
        plt.plot(x, u[i], label="Crank-Nicolson")
        plt.plot(x, stationary_distribution(x, omega, T), label="Equilibrium")
        plt.xlabel("I")
        plt.ylabel("Probability distribution")
        plt.title("Action Variable, t = {:.2f}".format(i * dt))
        plt.legend()
        # Save
        plt.tight_layout()
        plt.savefig("crank_time_uniform/foo" + str(i).zfill(5) + ".jpg", dpi=dpi)
        plt.clf()

# Make video
filename = "crank_time_uniform"
os.system("ffmpeg -y -i \"crank_time_uniform\\foo%05d.jpg\" " + filename +
          ".m4v")

# aiuto... """