""" This script tests the basic crypt for an number.
"""

import unittest
import sys
sys.path.insert(0, '..')

from BaseCrypt import BaseCrypt


class BaseCryptTests(unittest.TestCase):
    """
    Tests for `BaseCrypt.py`.
    """

    def test_base_62(self):
        """
        Test the base 62 of: 42, 141, 416, 7347
        """
        self.assertTrue(BaseCrypt.base_62(42) == 'g')
        self.assertFalse(BaseCrypt.base_62(42) == 'bad')

        self.assertTrue(BaseCrypt.base_62(141) == '2H')
        self.assertFalse(BaseCrypt.base_62(141) == 'bad')

        self.assertTrue(BaseCrypt.base_62(416) == '6i')
        self.assertFalse(BaseCrypt.base_62(416) == 'bad')

        self.assertTrue(BaseCrypt.base_62(7347) == '1uV')
        self.assertFalse(BaseCrypt.base_62(7347) == 'bad')

    def test_get_hash(self):
        """
        Test the values of 1, 41, 733, 82821, 467343
        """
        self.assertTrue(BaseCrypt.get_hash(1) == 'cJio3')
        self.assertFalse(BaseCrypt.get_hash(1) == 'bad')

        self.assertTrue(BaseCrypt.get_hash(41) == 'L2d5z')
        self.assertFalse(BaseCrypt.get_hash(41) == 'bad')

        self.assertTrue(BaseCrypt.get_hash(733) == '1AjhT')
        self.assertFalse(BaseCrypt.get_hash(733) == 'bad')

        self.assertTrue(BaseCrypt.get_hash(82821) == 'C1VlT')
        self.assertFalse(BaseCrypt.get_hash(82821) == 'bad')

        self.assertTrue(BaseCrypt.get_hash(467343) == 'rYWFN')
        self.assertFalse(BaseCrypt.get_hash(467343) == 'bad')

if __name__ == '__main__':
    unittest.main()

