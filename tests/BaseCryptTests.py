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

    def test_1(self):
        """
        Is cJio3 the base crypt of 1?
        """
        self.assertTrue(BaseCrypt.get_hash(1) == 'cJio3')
        self.assertFalse(BaseCrypt.get_hash(1) == 'bad')

    def test_41(self):
        """
        Is L2d5z the base crypt of 41?
        """
        self.assertTrue(BaseCrypt.get_hash(41) == 'L2d5z')
        self.assertFalse(BaseCrypt.get_hash(41) == 'bad')

    def test_733(self):
        """
        Is 1AjhT the base crypt of 733?
        """
        self.assertTrue(BaseCrypt.get_hash(733) == '1AjhT')
        self.assertFalse(BaseCrypt.get_hash(733) == 'bad')

    def test_82821(self):
        """
        Is C1VlT the base crypt of 82821?
        """
        self.assertTrue(BaseCrypt.get_hash(82821) == 'C1VlT')
        self.assertFalse(BaseCrypt.get_hash(82821) == 'bad')

    def test_467343(self):
        """
        Is rYWFN the base crypt of 467343?
        """
        self.assertTrue(BaseCrypt.get_hash(467343) == 'rYWFN')
        self.assertFalse(BaseCrypt.get_hash(467343) == 'bad')

if __name__ == '__main__':
    unittest.main()

