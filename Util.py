"""Util Module"""

import signal
import sys


def signal_handler(sig, frame):
    """Catch the CTRL+C signal"""
    print '\nAborted: ' + str(sig) + str(frame)
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)


def zerofill(number, size=8):
    """ return the number with zeros filled
        :param number: The number
        :param size: The size
        :return string
    """
    return str(number).zfill(size)
