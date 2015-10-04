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
    """
    BaseCrypt module class
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

    CHARS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

    BASE = len(CHARS)

    def __init__(self):
        pass

    @staticmethod
    def base_62(num):
        """
        * base_62()
        * Convert the number to base 62
        *
        * num: The number to encode
        * return: String
        """
        if (num == 0):
          return BaseCrypt.CHARS[0]

        length = BaseCrypt.BASE
        ret = ''
        while num != 0:
            ret = BaseCrypt.CHARS[int(num) % length] + ret
            num /= length

        return ret

    @staticmethod
    def get_hash(num, length=5):
        """
        * getHash()
        * Get the hash
        *
        * @param    Integer    num   A number
        * @param    Integer    length Maximum length of the hash
        * @return    String
        """

        length = 7 if length > 7 else (1 if length == 0 else abs(length))
        ceil = pow(62, length)
        prime = BaseCrypt.PRIMES[length]
        nb = (num * prime) - floor(num * prime / ceil) * ceil
        ret = BaseCrypt.base_62(nb)
        length *= -1
        return ret[length:]
