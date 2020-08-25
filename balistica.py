import scipy as sp
from scipy.integrate import odeint


cm=0.01
inch=2.54*cm

p = 1.225
cd = 0.47
D=8.5*inch
r= D/2
A=sp.pi * r**2
CD = 0.5*p*cd*A
m= 15 #kg
g = 9.81
viento0=10
viento1 =20

def bala0(z,t):
    zp = sp.zeros(4)
    zp[0]=z[2]
    zp[1]=z[3]

    v=z[2:4]


    v2= sp.dot(v,v)
    vnorm= sp.sqrt(v2)
    FD = (-CD)*v2*(v / vnorm)
    zp[2]=FD[0] /m
    zp[3]=FD[1] /m-g
    return zp
def bala1(z,t):
    zp = sp.zeros(4)
    zp[0]=z[2]
    zp[1]=z[3]

    v=z[2:4]
    v[0]=v[0]-viento0

    v2= sp.dot(v,v)
    vnorm= sp.sqrt(v2)
    FD = (-CD)*v2*(v / vnorm)
    zp[2]=FD[0] /m
    zp[3]=FD[1] /m-g
    return zp
def bala2(z,t):
    zp = sp.zeros(4)
    zp[0]=z[2]
    zp[1]=z[3]

    v=z[2:4]
    v[0]=v[0]-viento1

    v2= sp.dot(v,v)
    vnorm= sp.sqrt(v2)
    FD = (-CD)*v2*(v / vnorm)
    zp[2]=FD[0] /m
    zp[3]=FD[1] /m-g
    return zp

t=sp.linspace(0,30,1001)
veltiro=100

v0 = veltiro*1000./3600

z0=sp.array([0,0,v0,v0])


sol1= odeint(bala0,z0,t)
sol2= odeint(bala1,z0,t)
sol3= odeint(bala2,z0,t)

import matplotlib.pylab as plt

x= sol1[:,0]
y= sol1[:,1]
x1= sol2[:,0]
y1= sol2[:,1]
x2= sol3[:,0]
y2= sol3[:,1]
plt.figure(1)
plt.plot(x,y,label="viento =0")
plt.plot(x1,y1,label="viento =10m/s")
plt.plot(x2,y2,label="viento =20m/s")
plt.xlabel("X(m)")
plt.ylabel("Y(m)")
plt.title("Trayectoria para distintos vientos")
plt.legend(loc=0)
plt.grid(True)
plt.show()
