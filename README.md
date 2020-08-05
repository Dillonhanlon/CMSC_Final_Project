# CMSC_Final_Project - Maelstrom
## Dependencies
### In order to run this package and the corresping .py files, you need the following modules. 
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
### Note it is best to install `lightkurve` using conda so that all of its dependencies can be installed, so :
        conda install --channel conda-forge lightkurve
### However, if you must download with pip, then you should run the following commands:
        pip install lightkurve --upgrade
### or
        pip install lightkurve[all]
### If you still run into problems then you must install with conda. For more information see https://docs.lightkurve.org/about/install.html .

### Install Maelstrom from the source
        git clone --recursive https://github.com/danhey/maelstrom.git
        cd maelstrom
        python setup.py install

## Run `make` to obtain the results for this project. This produces a `report.pdf` file as well as multiple figures. This workflow may take a few minutes to run. 

## Note: when running `make` you may encounter some warnings, these are due to one of the modules (astropy) updating its code which Maelstrom uses. This does not affect the project.

# What is Maelstrom used for ? 

### *Maelstrom* is a package that was created by Daniel Hey (Paper: `Hey, Daniel R., et al. "Maelstrom: A Python package for identifying companions to pulsating stars from their light travel time variations." Journal of Open Source Software 5.51 (2020): 2125` [pdf](https://www.theoj.org/joss-papers/joss.02125/10.21105.joss.02125.pdf) ) for modelling and analyzing binary light curves. 

### When a star that begins pulsating when in orbit with another astronomical object, the time taken for these pulsations to reach us changes as a function of time. Understanding the phase of these pulsations can be used to obtain information about the star throughout the orbit. This method is know as *Phase Modulation*.

### *Maelstrom* uses a set of custom PyMC3 Models and solvers for modelling binary star orbits through phase modulation. Unlike previous methods, *Maelstrom* fits each individual datapoint in the time series by forward modelling the time delay onto the light curve.

### Data used in Maelstrom can be obtained online at https://mast.stsci.edu/portal/Mashup/Clients/Mast/Portal.html. However this data can be downloaded using the Python package *lightkurve*. For this project the python file `LK.py` extracts the light curve data using this module.

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

### In this project we are focusing on understanding how the brightness (or flux) changes with time in binary star systems and what information we can obtain from this. 

### The python files `LK.py`, `orbit.py`, `Recover_Binary.py`, `Maelstrom_lightcurve.py`, and `Maelstrom_TimeDelay.py` produces all the results for this project. 

 # Summary
 ### The python file `LK.py` finds a light curve and produces a figure for the brightness (flux) as a function of time for a star in binary. `Recover_Binary.py` outputs a pixel image of the star. The python files `Maelstrom_lightcurve.py`, and `Maelstrom_TimeDelay.py` produces iofthe lightcurve  deruved by forward modelling, as well produces a time delay versus time plot. Finally, `orbit.py` produces a very simplistic image of the estimated ellipse for the pulsating star with also the estimation of the barycenter for the binary system.
