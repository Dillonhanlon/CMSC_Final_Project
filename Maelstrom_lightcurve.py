import numpy as np
import corner
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import exoplanet as xo
import pymc3 as pm
import lightkurve as lk
import maelstrom as ms

from maelstrom import Maelstrom

from matplotlib import rcParams
mpl.rcParams['axes.linewidth'] = 1.2
rcParams["figure.dpi"] = 150
rcParams["savefig.dpi"] = 150


from LK import LC 

from maelstrom import Maelstrom
ms = Maelstrom(LC.time, LC.flux, max_peaks=5, fmin=5, fmax=48)
# ms.first_look()

print(f"Oscillation modes are at {ms.freq}")

period_guess = ms.get_period_estimate()
print(f"The orbital period is around {period_guess:.2f} days")

ms.setup_orbit_model(period=period_guess)
opt = ms.optimize()

td_time, td_td = ms.get_time_delay()
td_average = np.average(td_td, axis=-1, weights=ms.get_weights())

plt.figure(figsize=(8,8))
with ms:
    plt.plot(ms.time, xo.eval_in_model(ms.lc_model, opt), c='blue', linewidth=0.5, label='Maelstrom')
    plt.plot(ms.time, ms.flux, '.k', label='Data')
    plt.xlim(200,205)
    plt.ylim(-6,6)
    plt.savefig('lightcurve_opt.png')
# plt.xlim(200,205)
plt.xlabel('Time [day]')
plt.ylabel('Flux [ppt]')
plt.legend()

