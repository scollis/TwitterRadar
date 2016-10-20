"""
=====================================
twitter (:mod:`twitterradar.twitter`)
=====================================

.. currentmodule:: twitterradar.twitter

Tools for using the twitter api in python

API Tools
=========

.. autosummary::
    :toctree: generated/

    api_from_json
"""

from .api_tools import api_from_json

__all__ = [s for s in dir() if not s.startswith('_')]


