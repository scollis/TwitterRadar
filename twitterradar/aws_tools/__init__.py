"""
=========================================
aws_tools (:mod:`twitterradar.aws_tools`)
=========================================

.. currentmodule:: twitterradar.aws_tools

Tools for using the Amazon Web Services with twitter and
Py-ART

Amazon tools
============

.. autosummary::
    :toctree: generated/

    get_radar_from_aws
"""

from .nexrad_boto import get_radar_from_aws

__all__ = [s for s in dir() if not s.startswith('_')]



