#!/usr/bin/env python
"""
PURPOSE: For handling variables in within the website
"""
# ########################################################################### #

import unittest

class Namespace (object):
    """ Empty Namespace object which can have arbitrary attributes """
    pass 

class Link (object):
    """ A particular link """

    def __init__ (self,url,text):
        self.url = url 
        self.text = text 

    def to_html (self,tmp='<a class="{css_class}" href="{url}">{text}</a>',css_class=""):
        kws = dict(\
            url=self.url,
            text=self.text,
            css_class=css_class,
            )
        return tmp.format(**kws)

class TestLink (unittest.TestCase):

    def test_link (self):

        url = "hello"
        text = "world"
        tmp = '<a href="{url}">{text}</a>'

        link = Link(url, text)
        sol = tmp.format(url=url,text=text)
        ans = link.to_html()
        assert sol==ans 
        assert link.url == url 
        assert link.text == text 

