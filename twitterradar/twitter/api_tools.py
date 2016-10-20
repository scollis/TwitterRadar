"""
pyart.twitter.api_tools
=========================

Some time saving tools for working with the twitter API

.. autosummary::
    :toctree: generated/

    api_from_json
"""

import json
import twitter

def api_from_json(filename):
    """
    return a twitter API hande from a JSON file
    Format should be:
    {"consumer_key":"SOMETHING",
    "consumer_secret":"SOMETHINGELSE",
    "access_token_key":"ANOTHERTHING",
    "access_token_secret":"YETANOTHERTHING"}
    See https://python-twitter.readthedocs.io/en/latest/getting_started.html
    for instructions

    Parameters
    ----------
    filename: string
        location of file

    Returns
    -------
    twitter_api: twitter_api
        api for using twitter with the credential suppiled in the file

    """
    fh = open(filename)
    myson = json.load(fh)
    fh.close()
    twitter_api = twitter.Api(consumer_key=myson['consumer_key'],
                  consumer_secret=myson['consumer_secret'],
                  access_token_key=myson['access_token_key'],
                  access_token_secret=myson['access_token_secret'])
    return twitter_api

