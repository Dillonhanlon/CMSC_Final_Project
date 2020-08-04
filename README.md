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
        ix)     theano


### To download these modules either using conda or pip you can use the following format 
        pip(3) install exoplanet
        pip(3) install pymc3
        pip(3) install astropy
        pip(3) install lightkurve
        pip(3) install pandas
        pip(3) install numpy
        pip(3) install matplotlib
        pip(3) install corner
        pip(3) install theano

or 

        conda install exoplanet pymc3 astropy lightkurve etc. 

### Install Maelstrom from the source
        git clone --recursive https://github.com/danhey/maelstrom.git
        cd maelstrom
        python setup.py install

## Run `make` to obtain the results for this project. This produces a `report.pdf` file as well as multiple figures.

## Note: when running `make` you may encounter some warnings, these are due to one of the modules (astropy) updating its code which Maelstrom calls uses. The program still runs normally.

# What is Maelstrom used for ? 

### *Maelstrom* is a package that was created by Daniel Hey (DOI: https://joss.theoj.org/papers/10.21105/joss.02125) for modelling and analyzing binary light curves. When a star that begins pulsating when in orbit with another astronomical object, the time taken for these pulsations to reach us changes as a function of time. Understanding the phase of these pulsations can be used to obtain information about the star throughout the orbit. This method is know as *Phase Modulation*.

### *Maelstrom* uses a set of custom PyMC3 Models and solvers for modelling binary star orbits through phase modulation. Unlike previous methods, *Maelstrom* fits each individual datapoint in the time series by forward modelling the time delay onto the light curve.

### Data used in Maelstrom can be obtained online at https://mast.stsci.edu/portal/Mashup/Clients/Mast/Portal.html. However this data can be downloaded using the Python package *lightkurve*. For this project the python filev`LK.py` extracts the light curve data by means of the *lightkurve* module.

# How to use Maelstrom?

### First to start a project with *Maelstrom* a light curve must be downloaded, and to do this as mentioned previously all you need to do is run the file 
        LK.py
### the default light curve for this project is set to data from "KIC 8264492" (Note: KIC = Kepler Input Catalogue). But if you wish to change this to another mission all you need to do is change the 
        input 
### in
        LK.py
### to another light curve. For example, if you are interested in the binary star system KIC 9651065, then you would change 
        input = "KIC 9651065"
        mission = "Kepler"
in 

        LK.py
### and then run the file.

### NOTE: When changing the `input`, some of the parameters in the other python files, `Maelstrom_Frequency.py`  and `Recover_Planet.py` may also need to change. Those parameters being "`fmin`" and "`fmax`" in `Maelstrom_Frequency.py` and "`period` range" in `Recover_Planet.py`. 

## Analyzing light curve data

### In this project we are focusing on understanding how the brightness (or flux) changes with time in binary star systems and what information we can obtain from this. First a pixel image of the star is created using the `lightkurve` module in the python file `Recover_Planet.py`

### The python file `Maelstrom_Frequency.py` output initial plots of  i) the light curve ii) the amplitude spectrum iii) the extracted time delays, and iv) the periodogram of the time delays. This python file also uses a forward modelling routine as part of the `Maelstrom` package for light curve. The results (plots) of the forward modelling is saved as `pdf` files with the appropriate name. `Maelstrom_Frequency.py` also prints the orbital period for the star and its oscillation modes.

 # Summary
 ### The python file `LK.py` finds a light curve for a star in binary. `Recover_Planet.py` outputs a pixel image of the star. The python file `Maelstrom_Frequency.py` produces inital plots based on the lightcurve and models the data by means of forward modelling and produces results in the form of plots.
