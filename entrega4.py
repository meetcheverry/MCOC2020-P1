from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import math
a=2
def zp(z,t):
    return a*z
def eulerint(zp,zo,t,Nsubdivisiones):
    Nt = len(t)
    Ndim= len(np.array([z0]))

    z= np.zeros((Nt,Ndim))
    z[0,:] = z0
    for i in range(1,Nt):
        t_anterior = t[i-1]
        dt= (t[i] - t[i-1])/Nsubdivisiones
        z_temp=  z[i-1,:].copy()
        for k in range(Nsubdivisiones):
            z_temp += dt * zp(z_temp, t_anterior+ k*dt)
        z[i,:] = z_temp

    return z
z0=1
t= np.linspace(0,4.,100)

sol = odeint(zp,z0,t )
z_odeint = sol[:,0]
z_real = z0*np.exp(a*t)

sol = eulerint(zp,z0,t,1 )
z_euler1 = sol[:,0]

sol = eulerint(zp,z0,t,10 )
z_euler10 = sol[:,0]

sol = eulerint(zp,z0,t,100)
z_euler100 = sol[:,0]
#Grafico
plt.plot(t,z_odeint, label="Odeint",color="b")
plt.plot(t,z_euler1,"--", label="EulerInt, N=1",color="g")
plt.plot(t,z_euler10,"--", label="EulerInt, N=10",color="R")
plt.plot(t,z_euler100,"--", label="EulerInt, N=100",color="Orange")
plt.plot(t,z_real, label="Real",color="k",linewidth=2)

plt.legend()
plt.show()
