"""
pyart.reduction.statistics
==========================

Statistics of radar volumes

.. autosummary::
    :toctree: generated/

    min_max
    ngates_above
"""

import numpy as np

def min_max(radar, variable):
    """
    return the minimum and maximum value of field variable
    from the radar

    Parameters
    ----------
    radar: Py-ART radar object
        Radar from which to work out min/max

    variable: string
        variable name

    Returns
    -------
    (min, max): floats
        minimum and maximum values of the field

    """
    minm = radar.fields[variable]['data'].min()
    maxm = radar.fields[variable]['data'].max()
    return (minm, maxm)

def ngates_above(radar, variable, value):
    """
    Return the number of gates above a certain value
    in a certain field

    Parameters
    ----------
    radar: Py-ART radar object
        Radar from which to work out ngates

    variable: string
        variable name

    value: float
        The value of which n_gates are over

    Returns
    -------
    ngates: integer
        number of gates above value in radar
    """
    positions = np.where(radar.fields[variable]['data'] > value)
    n_gates = len(positions[0])
    return n_gates


