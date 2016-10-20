"""
twitterradar: The Python Twitter Radar Robot
============================================

"""
try:
    __TWITTERRADAR_SETUP__
except NameError:
    __TWITTERRADAR__ = False

if __TWITTERRADAR__:
    import sys as _sys
    _sys.stderr.write("Running from TwitterRadar source directory.\n")
    del _sys
else:
    import warnings as _warnings
    _warnings.simplefilter("always", DeprecationWarning)

    # import subpackages
    from . import plotting
    from . import reduction
    from . import twitter
    from . import aws_tools
    from . import core
    from .core import tweet_my_radar

