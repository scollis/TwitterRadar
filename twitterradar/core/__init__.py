"""
===============================
core (:mod:`twitterradar.core`)
===============================

.. currentmodule:: twitterradar.core

Core utilities for tweeting your radar

Tools
=====

.. autosummary::
    :toctree: generated/

    tweet_my_radar
"""

from .tools import tweet_my_radar

__all__ = [s for s in dir() if not s.startswith('_')]


