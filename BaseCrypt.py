"""
This script creates a basic crypt for an number.

BaseCrypt Class [ BaseCrypt.py ]

@author      Eric Potvin
@package     PythonLib
@subpackage  Encryption
@link        https://github.com/ericpotvin/PythonLib
"""

from math import floor


class BaseCrypt(object):
    """ BaseCrypt module class
    """

    PRIMES = [
        1,
        41,
        2377,
        147299,
        9132313,
        566201239,
        35104476161,
        2176477521929
    ]

    chars = {
        0: 48, 1: 49, 2: 50, 3: 51, 4: 52, 5: 53, 6: 54, 7: 55, 8: 56,
        9: 57, 10: 65, 11: 66, 12: 67, 13: 68, 14: 69, 15: 70, 16: 71,
        17: 72, 18: 73, 19: 74, 20: 75, 21: 76, 22: 77, 23: 78, 24: 79,
        25: 80, 26: 81, 27: 82, 28: 83, 29: 84, 30: 85, 31: 86, 32: 87,
        33: 88, 34: 89, 35: 90, 36: 97, 37: 98, 38: 99, 39: 100, 40: 101,
        41: 102, 42: 103, 43: 104, 44: 105, 45: 106, 46: 107, 47: 108,
        48:109, 49: 110, 50: 111, 51: 112, 52: 113, 53: 114, 54: 115,
        55: 116, 56: 117, 57: 118, 58: 119, 59: 120, 60: 121, 61: 122
    }

    @classmethod
    def base_62(cls, i):
        """ Convert the number to base 62
            :param i: A number
            :return String
        """
        key = ''
        while i > 0:
            key += chr(cls.chars[(i - (floor(i / 62) * 62))])
            i = floor(i/62)
        return key[::-1]

    @staticmethod
    def get_hash(num, length=5):
        """ Get the hash
            :param num: A number
            :param length: Maximum length of the hash
            :return String
        """

        length = 7 if length > 7 else (1 if length == 0 else abs(length))
        ceil = pow(62, length)

        prime = BaseCrypt.PRIMES[length]
        ret = BaseCrypt.base_62(
            (num * prime) - floor(num * prime / ceil) * ceil)
        return ret.ljust(length, "0")
