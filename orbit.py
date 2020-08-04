import numpy as np
from matplotlib import pyplot as plt
from math import pi

from Maelstrom_lightcurve import opt
eccen = np.mean(opt['eccen'])
a = np.mean(opt['lighttime'])
b = a / 2
rmean = (a * (eccen))

u=0     #x-position of the center
v=0    #y-position of the center
u1 = a

t = np.linspace(0, 2*pi, 100)
fig, ax = plt.subplots(figsize = (10,10))
plt.plot(u+a*np.cos(t) , v+b*np.sin(t), label = 'Binary star orbit' )
plt.plot(rmean , 0, 'ro', markersize=14, label = 'Barycenter')
ax = plt.gca()
ax.axes.xaxis.set_visible(False)
ax.axes.yaxis.set_visible(False)
ax.axhline(c='grey',linestyle = '--', lw=1,label = 'Equitorial Plane')
ax.legend()
plt.savefig('orbit.png')
