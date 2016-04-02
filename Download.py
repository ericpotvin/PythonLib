"""
Download module

Download Class [ Download.py ]

@author      Eric Potvin
@package     PythonLib
@subpackage  Download
@link        https://github.com/ericpotvin/PythonLib
"""
import urllib2


def download_page(url):
    """ Download a web page
        :param url: The website URL
    """
    data = urllib2.urlopen(url)
    return data.read()
