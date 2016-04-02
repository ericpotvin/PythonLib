"""
HTML Cleaner module

HTMLCleaner Class [ HTMLCleaner.py ]

@author      Eric Potvin
@package     PythonLib
@subpackage  HTML
@link        https://github.com/ericpotvin/PythonLib
"""
from collections import OrderedDict
from re import sub, DOTALL


class HTMLCleaner(object):
    """ HTML module
    """

    def __init__(self, tags):
        """ Init
            :param tags: The unwanted HTML tags
        """
        self.tags = tags

    def clean(self, content):
        """ Remove unwanted HTML tags
            :param content: The HTML content
            :return string
        """

        if self.tags is None:
            return content

        for (_from, _to) in self.tags.items():
            content = sub(_from, _to, content, flags=DOTALL)

        return content.strip()

    @staticmethod
    def get_common_tags():
        """ Get the common HTML tags
        """
        replace = OrderedDict()

        # remove non ascii
        replace[r"[^\x00-\x7f]"] = ""

        # html
        replace["<html(.*?)>"] = ""
        replace["</html>"] = ""
        replace["<head(.*?)>"] = ""
        replace["</head>"] = ""
        replace["<body(.*?)>"] = ""
        replace["</body>"] = ""
        replace["<meta (.*?)>"] = ""
        replace["<!DOCTYPE html>"] = ""
        replace["<title>"] = ""
        replace["</title>"] = ""
        replace["&nbsp;"] = ""
        # CSS
        replace["<link (.*?)>\n"] = ""
        # JS
        replace["<script>(.*?)</script>"] = ""
        replace["<noscript>(.*?)</noscript>"] = ""
        replace["<script(.*?)</script>"] = ""
        # forms
        replace["<select(.*?)>(.*?)</select>"] = ""
        replace["<form(.*?)>(.*?)</form>"] = ""
        replace["<button(.*?)>(.*?)</button>"] = ""
        replace["<input(.*?)>"] = ""

        # Comments
        replace["<!--( ?)(.*?)>\n"] = ""
        replace[r"<![endif]-->"] = ""

        return replace

    @staticmethod
    def get_layout_tags():
        """ Get the style HTML tags we need to remove
        """
        replace = OrderedDict()

        replace["<ul(.*?)>"] = ""
        replace["</ul>"] = ""
        replace["<li(.*?)>"] = ""
        replace["</li>"] = ""
        replace["<div(.*?)>"] = ""
        replace["</div>"] = ""
        replace["<p(.*?)>"] = ""
        replace["</p>"] = ""
        replace["<span(.*?)>"] = ""
        replace["</span>"] = ""
        replace["<nav(.*?)>(.*?)</nav>"] = ""

        return replace

    @staticmethod
    def get_style_tags():
        """ Get the style HTML tags we need to remove
            For now we only need H1
        """
        replace = OrderedDict()

        replace["<h1(.*?)>"] = ""
        replace["</h1>"] = ""
        replace["<h2(.*?)>(.*?)</h2>"] = ""
        replace["<h3(.*?)>(.*?)</h3>"] = ""
        replace["<h4(.*?)>(.*?)</h4>"] = ""
        replace["<h5(.*?)>(.*?)</h5>"] = ""
        replace["<h6(.*?)>(.*?)</h6>"] = ""
        replace["<i(.*?)>"] = ""
        replace["</i>"] = ""
        replace["<u(.*?)>"] = ""
        replace["</u>"] = ""

        return replace

    @staticmethod
    def clean_up_tags():
        """ Clean up tags, layout, etc..
        """
        replace = OrderedDict()

        replace[": "] = ":"
        replace["<img "] = "\n<img "
        replace['<img alt="(.*?)" '] = "<img "
        replace['\n\n\t'] = " "
        replace['/>'] = "/>\n"
        replace[":\n"] = ": "
        replace["<img  "] = "<img "

        return replace
