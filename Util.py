"""Util Module"""

import signal
import sys


def signal_handler(sig, frame):
    """Catch the CTRL+C signal"""
    print '\nAborted: ' + str(sig) + str(frame)
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

