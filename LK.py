import numpy as np
import matplotlib.pyplot as plt
import exoplanet as xo
import lightkurve as lk
from lightkurve import search_lightcurvefile


input = "KIC 8264492"
mission = "Kepler"
label = input
quarter = 1
LC = lk.search_lightcurvefile(input, mission=mission).download_all().PDCSAP_FLUX.stitch().remove_nans()

tpf = lk.search_targetpixelfile(input).download()

LC.plot()
plt.savefig('Lightcurve.pdf')


