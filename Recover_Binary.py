import lightkurve as lk
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams['axes.linewidth'] = 1.2

from LK import tpf
from LK import label

tpf.plot(frame=100, scale='log', show_colorbar=True)
plt.title('KIC 8264492',fontsize = 14)
plt.xlabel('Pixel Column Number [No Units]')
plt.ylabel('Pixel Row Number [No Units]')
plt.savefig('Recover_Binary.png')
