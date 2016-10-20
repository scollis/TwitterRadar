

def configuration(parent_package='', top_path=None):
    from numpy.distutils.misc_util import Configuration
    config = Configuration('twitterradar', parent_package, top_path)
    config.add_subpackage('plotting')
    config.add_subpackage('reduction')
    config.add_subpackage('twitter')
    config.add_subpackage('aws_tools')
    config.add_subpackage('core')

    return config

if __name__ == '__main__':
    from numpy.distutils.core import setup
    setup(**configuration(top_path='').todict())
