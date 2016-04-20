""" This script tests the basic crypt for an number.
"""

import unittest
import sys
from HTMLCleaner import HTMLCleaner

sys.path.insert(0, '..')

# TODO: Need more TESTS


class HTMLCleanerTests(unittest.TestCase):
    """
    Tests for `HTMLCleanerTests.py`.
    """

    def test_common_tags(self):
        """ test get_common_tags
        """
        html = "<!DOCTYPE html>\n" + \
               "<html>" + \
               "<head><title>TEST</title></head>" + \
               "<body>" + \
               "</body></html>"
        tags = HTMLCleaner.get_common_tags()
        clean_html = HTMLCleaner(tags)
        self.assertTrue(clean_html.clean(html) == "TEST")

    def test_layout_tags(self):
        """ test get_common_tags
        """
        html = "<span></span>" + \
               "<p>" + \
               "</p>" + \
               "<ul><li>TEST</li></ul>" + \
               "<nav id='test'><p> should be removed</p></nav>"
        tags = HTMLCleaner.get_layout_tags()
        clean_html = HTMLCleaner(tags)
        self.assertTrue(clean_html.clean(html) == "TEST")

    def test_style_tags(self):
        """ test get_common_tags
        """
        html = "<h1>Hello</h1>" + \
               "<h2>hi</h2>" + \
               "<u></u>" + \
               "<h6>1</h6>"
        tags = HTMLCleaner.get_style_tags()
        clean_html = HTMLCleaner(tags)

        self.assertTrue(clean_html.clean(html) == "Hello")

    def test_cleanup_tags(self):
        """ test get_common_tags
        """
        html = ": "
        tags = HTMLCleaner.clean_up_tags()
        clean_html = HTMLCleaner(tags)
        self.assertTrue(clean_html.clean(html) == ":")

        html = "<img  src='#'>"
        tags = HTMLCleaner.clean_up_tags()
        clean_html = HTMLCleaner(tags)
        self.assertTrue(clean_html.clean(html) == "<img src='#'>")

if __name__ == '__main__':
    unittest.main()
