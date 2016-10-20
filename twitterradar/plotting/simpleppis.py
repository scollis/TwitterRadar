"""
pyart.plotting.simpleppis
=========================

Simple plotting of ppis and saving to temporary files

.. autosummary::
    :toctree: generated/

    very_simple_ppi
"""

import matplotlib.pyplot as plt
import numpy as np
import tempfile
from pyart.graph import RadarMapDisplay, cm

def very_simple_ppi(radar,  min_lat = None,
                  max_lat = None, min_lon = None,
                  max_lon = None):
    """
    Plot a radar file and return the location

    Parameters
    ----------
    radar: Py-ART radar object
        Radar to be plotted

    min_lat, max_lat, min_lon, max_lon: floats
        bounds for the display

    Returns
    -------
    radar_location: string
        Location of the image file

    """
    display = RadarMapDisplay(radar)
    fig = plt.figure(figsize = [10,8])

    #Plot Z from lowest tilt
    display.plot_ppi_map('reflectivity', sweep = 0, resolution = 'i',
                        vmin = -8, vmax = 64, mask_outside = False,
                        cmap = cm.NWSRef,
                        min_lat = min_lat, min_lon = min_lon,
                        max_lat = max_lat, max_lon = max_lon)

    #get a tempfile
    localfile = tempfile.NamedTemporaryFile()

    #Save to tempfile.. Need png or Twitter gets grumpy
    plt.savefig(localfile.name + '.png')
    return localfile.name + '.png'
