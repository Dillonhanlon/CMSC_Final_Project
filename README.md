# CMSC_Final_Project - Maelstrom
## Dependencies
### In order to run this package and the corresping .py files, you need the following modules. I recommend using conda to install instead of pip since some of the modules have dependencies themself that can only be installed using conda (i.e lightkurve); 
        i)      exoplanet 
        ii)     pymc3
        iii)    astropy
        iv)     lightkurve
        v)      pandas
        vi)     numpy
        vii)    matplotlib
        viii)   corner


### To download these modules using conda you can use the following format 
        conda install exoplanet
        conda install pymc3
        conda install astropy
        conda install lightkurve
        conda install pandas
        conda install numpy
        conda install matplotlib
        conda install corner

or 

        conda install exoplanet pymc3 astropy lightkurve etc. 

### Installing from the source
        git clone --recursive https://github.com/danhey/maelstrom.git
        cd maelstrom
        python setup.py install



# What is Maelstrom used for ? 
### *Maelstrom* is a package that was created by Daniel Hey (DOI: https://joss.theoj.org/papers/10.21105/joss.02125) for modelling and analyzing binary light curves. When a star that begins pulsating when in orbit with another astronomical object, the time taken for these pulsations to reach us changes as a function of time. Understanding the phase of the these pulsations can be used to obtain information about the star throughout the orbit. This is know as *Phase Modulation*.

### *Maelstrom* uses a set of custom PyMC3 Modelsand solvers for modelling binary orbits through phase modulation. Unlike previous methods, *Maelstrom* fits each individual datapoint in the time series by forward modelling the time delay onto the light curve.

### Data used in Maelstrom can be obtained for free to the public for *Kepler* and *TESS* missions. This data is available online at https://mast.stsci.edu/portal/Mashup/Clients/Mast/Portal.html. However this data can be downloaded using the Python package *lightkurve*, for this project this data can be downloaded using the Python file LK.py.

# How do I use Maelstrom?
### First to start a project with *Maelstrom* a light curve must be downloaded, and to do this as mentioned previously all you need to do is run the file 
        LK.py
### the default lightcurve is set to data from "KIC 8264492". But if you wish to change this to another mission all you need to do is change the 
        input 
### in
        LK.py
### to another mission. For example, if you are interested in the binary star system KIC 9651065, then you would change 
        input = "KIC 9651065"
        mission = "Kepler"
### and then run the file. Of course you can also just run `make` as mentioned previously.

### NOTE: When changing the `input`, some of the parameter in the other files, `Maelstrom_Frequency.py`  and `Recover_Planet.py` you may also need to change `fmin` and `fmax` in `Maelstrom_Frequency.py` and period range in `Recover_Planet.py`. 

### Now we can begin by analysing lightcurves

### In this project we are focusing on understanding how the brightness (or flux) changes with time in binary star systems. First a pixel image of the star is created using the `lightkurve` module in the python file `Recover_Planet.py`

### The python file `Maelstrom_Frequency.py` output plots of first inital  plots which are; i) the light curve ii) the amplitude spectrum iii) the extracted time delays, and iv) the periodogram of the time delays. As well as the same plots after modelling the data are also given. The figures made from running this file with automatically save the plots as `pdf` files with the appropriate name. `Maelstrom_Frequency.py` also prints the orbital period for the star and the oscillation modes associated with the data.

 # Summary
 ### The python file `LK.py` finds a light curve for a star in binary. `Recover_Planet.py` outputs a pixel image of the star. The python file `Maelstrom_Frequency.py` produces inital plots based on the lightcurve. As well this file with model the light curve data and produce plots.
