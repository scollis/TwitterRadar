"""
=========================================
Reduction (:mod:`twitterradar.reduction`)
=========================================

.. currentmodule:: twitterradar.reduction

Create statistics from radar files

Statistics
==========

.. autosummary::
    :toctree: generated/

    min_max
    ngates_above
"""

from .statistics import min_max, ngates_above

__all__ = [s for s in dir() if not s.startswith('_')]


