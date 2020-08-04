import lightkurve as lk
import numpy as np
import matplotlib.pyplot as plt

from LK import tpf
from LK import label

tpf.plot(frame=100, scale='log', show_colorbar=True)
plt.savefig('Recover_Binary.png')
