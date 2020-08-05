import numpy as np
import matplotlib.pyplot as plt
import exoplanet as xo
import lightkurve as lk
from lightkurve import search_lightcurvefile
import matplotlib as mpl
from matplotlib import rcParams
mpl.rcParams['axes.linewidth'] = 1.2
rcParams["figure.dpi"] = 150
rcParams["savefig.dpi"] = 150


input = "KIC 8264492"
mission = "Kepler"
label = input
quarter = 1
LC = lk.search_lightcurvefile(input, mission=mission).download_all().PDCSAP_FLUX.stitch().remove_nans()

tpf = lk.search_targetpixelfile(input).download()
plt.figure(figsize = (8,8))

LC.plot()
plt.ylabel('Normalized Flux',fontsize = 16)
plt.xlabel('Time - 2454833 [BKJD day]',fontsize = 16)
plt.title('Normalized Flux vs Time [BKJD days]',fontsize = 16)
plt.savefig('Lightcurve.png')


