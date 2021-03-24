from scipy.integrate import quadrature
import numpy as np
import math

g = 9.8
v_t = 54.0 # in m/s
X = []
T = []

def Velocity(t, v_t):
    return v_t*(1-np.exp(-2*g*t/v_t))/(1+np.exp(-2*g*t/v_t))

dt = 0.001
t = 0
x = 4000 #in m
i = 0

while (x>1200):
    t = i*dt
    i += 1
    dx, err = quadrature(Velocity, 0, t, args=v_t)
    x = 4000 - dx
    X.append(str(x))
    T.append(str(t))

dt = 6.5E-7
t1 = t
i = 0
a = -15.467
print(str(t1) + " Check.")

while(v_t > 7.6):
    t = t1 + i*dt
    c = i*dt
    v_t = a*c + 54
    i += 1
    dx, err = quadrature(Velocity, t, t+dt, args=v_t)
    x = x - dx
    X.append(str(x))
    T.append(str(t))

dt = 0.001
i = 0
v_t = 7.6
t2 = t 
x2 = x
print(str(t2) + " Check.")

while (x>0):
    t = t2 + i*dt
    i += 1
    dx, err = quadrature(Velocity, t2, t, args=v_t)
    x = x2 - dx
    X.append(str(x))
    T.append(str(t))

t3 = t
print(str(t3) + " Check.")

outFile = open("JumpData.txt", "w")

for i in range(0, len(X)):
    outFile.write(str(T[i]) + " " + str(X[i]) + "\n")

outFile.close()