from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import math

hr = 3600. #s
km = 1e3 # m
Radio = 6371.*km #km
Mt= 5.972e24 #kg
G=6.67408e-11 #m3 kg-1 s-2
o= -7.2921150e-5 #rad/s
H0= 700.*km

FgMax = G*Mt/Radio**2

zp= np.zeros(6)

def zpunto(z,t):
    R= np.array([[math.cos(o*t),math.sin(o*t),0],[-math.sin(o*t),math.cos(o*t),0],[0,0,1]])
    R1= o * np.array([[-math.sin(o*t),math.cos(o*t),0],[-math.cos(o*t),-math.sin(o*t),0],[0,0,0]])
    R2= (o**2) * np.array([[-math.cos(o*t),-math.sin(o*t),0],[math.sin(o*t),-math.cos(o*t),0],[0,0,0]])

    z1=z[0:3] #x,y,z
    z2=z[3:6] #vx,vy,vz

    r2 = np.dot(z1,z1)
    r = np.sqrt(r2)

    Fg=((-G*Mt)/(r**2)) * (R@(z1/r))

    zp[0:3] = z2
    zp[3:6] = np.transpose(R)@(Fg - (2 * (R1@z2) + (R2@z1)))

    return zp

from datetime import datetime
ti = "2018-08-14T22:59:42.000000"
ti =ti.split("T")
ti = "{} {}".format(ti[0], ti[1])
ti = datetime.strptime(ti,'%Y-%m-%d %H:%M:%S.%f')

tf = "2018-08-16T00:59:42.000000"
tf = tf.split("T")
tf = "{} {}".format(tf[0], tf[1])
tf = datetime.strptime(tf,'%Y-%m-%d %H:%M:%S.%f')

deltaT = (tf - ti).seconds

x_i = 128091.735405
y_i = 6900016.545163
z_i =-1574955.311391

vx_i = 1567.020245
vy_i = -1674.007605
vz_i =-7239.572574

x_f = 1010095.475188
y_f = -123073.229951
z_f =-7008913.872221

vx_f = -1887.279838
vy_f = -7324.093741
vz_f =-143.308102

# vector tiempo
t=np.linspace(0 , deltaT , 9361)


z0 = np.array([x_i,y_i,z_i,vx_i,vy_i,vz_i])

sol = odeint(zpunto, z0, t)

x= sol[:,0:3]

pos_final= np.array([x_f,y_f,z_f,vx_f,vy_f,vz_f]) - sol[1]

print (f"Diferencia posicion x={pos_final[0]}")
print (f"Diferencia posicion y={pos_final[1]}")
print (f"Diferencia posicion z={pos_final[2]}")
exit()

H = np.sqrt(x[:,0]**2 + x[:,1]**2 + x[:,2]**2) - Radio

plt.figure()
for i in range(3):
    plt.subplot(3,1,1+i)
    plt.grid(True)
    plt.plot(t/hr,x[:,i])

plt.figure()
plt.grid(True)
plt.plot(t / hr, H / km)
plt.axhline(80., linestyle="--", color="#438EF6")
plt.axhline(0., linestyle="--", color="#824B01", linewidth=2)

plt.figure()
plt.grid(True)
plt.plot(x[:,0],x[:,1])

th = np.linspace(0,(2*(np.pi)),400)

pe= math.cos(th)
po= math.sin(th)
plt.plot(Radio * pe , Radio * po , color="#70531B" , linewidth=2)
plt.axis("equal")
plt.show()
