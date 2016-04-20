""" This script tests the basic crypt for an number.
"""

import unittest
import sys
from Util import zerofill

sys.path.insert(0, '..')


class UtilTests(unittest.TestCase):
    """
    Tests for `BaseCrypt.py`.
    """

    def test_zerofill(self):
        """ Test zerofill()
        """
        self.assertTrue(zerofill(1, 1) == "1")
        self.assertTrue(zerofill(1, 2) == "01")
        self.assertTrue(zerofill(1, 3) == "001")
        self.assertTrue(zerofill(1, 4) == "0001")

    def test_out_of_bound(self):
        """ test zerofill() out of bound
        """
        self.assertTrue(zerofill(1000, 0) == "1000")
        self.assertTrue(zerofill(1000, 1) == "1000")
        self.assertTrue(zerofill(1000, 2) == "1000")
        self.assertTrue(zerofill(1000, 3) == "1000")

if __name__ == '__main__':
    unittest.main()
