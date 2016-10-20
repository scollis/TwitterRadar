"""
=======================================
Plotting (:mod:`twitterradar.plotting`)
=======================================

.. currentmodule:: twitterradar.plotting

Create plots of radar files and saves to
temporary files

Simple PPIs
===========

.. autosummary::
    :toctree: generated/

    very_simple_ppi
"""

from .simpleppis import very_simple_ppi

__all__ = [s for s in dir() if not s.startswith('_')]

