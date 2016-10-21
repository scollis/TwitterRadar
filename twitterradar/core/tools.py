"""
=====================================
core (:mod:`twitterradar.core.tools`)
=====================================

.. currentmodule:: twitterradar.core

Tools for using the twitter api in python

Top level tweeting tools
========================

.. autosummary::
    :toctree: generated/

    tweet_my_radar
"""

from ..plotting.simpleppis import very_simple_ppi
from ..reduction.statistics import min_max, ngates_above
from ..aws_tools.nexrad_boto import get_radar_from_aws
from datetime import datetime
from twitter.error import TwitterError


def tweet_my_radar(site, tapi, datetime_string, fmat = '%Y%m%d_%H%M%S',
        min_lat = None, max_lat = None,
        min_lon = None, max_lon = None,
        postscript = None, length_error = None):
    """
    Fetch a radar from S3, plot it and tweet plus statistics.

    Grab a radar from a site and use the Twitter API
    to tweet the PPI from the lowest tilt to twitter.
    Also tweet the number of gates above two reflectivity
    thresholds and the min and max reflectivity.


    Parameters
    ----------
    site : string
        four letter radar designation

    datetime_string : string
        desired date time, use 'now' for now

    fmat : string
        datetime format

    min_lat, max_lat, min_lon, max_lon: floats
        bounds for the display

    Returns
    -------
    status : dictionary
        status from the twitter API

    """

    #Get a Py-ART radar Object
    if datetime_string.upper() == 'NOW':
        b_d = datetime.utcnow()
        gotime = True
    else:
        try:
            b_d = datetime.strptime(datetime_string, fmat)
            gotime = True
        except ValueError:
            gotime = False
    if gotime:
        my_radar = get_radar_from_aws(site, b_d)
        image_file = very_simple_ppi(my_radar)
        minm, maxm = min_max(my_radar, 'reflectivity')
        z40 = ngates_above(my_radar,  'reflectivity', 40.)
        z20 =  ngates_above(my_radar,  'reflectivity', 20.)
        gdata = " {0} gates above 20 {1} above 40dBZ".format(z20,
                z40)
        mmdata = "The min Z is {0}dBZ and the max is {1}dBZ".format(minm,
                                                             maxm)

        if postscript == None:
            postscript = ''
        else:
            postscript = ' ' + postscript
        try:
            status = tapi.PostUpdate( gdata + ' ' + mmdata + postscript,
                    media = image_file)
        except TwitterError:
            status = tapi.PostUpdate('Sorry, the message generated is too long.Try reducing your postscript')

    else:
        status = tapi.PostUpdate('Sorry, datetime is not valid. use now or YYYYMMDD_HHMMSS')
    return status


