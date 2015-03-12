#!/usr/bin/env python
"""
PURPOSE: This contains settings parameters associated with variables in the webpage
"""
# ########################################################################### #

from stock_up.settings.base import *
from stock_up.site_variables import Link, Namespace
from collections import OrderedDict

title = "StockUp"

links = Namespace()
setattr(links,"github_stock_up",Link("https://github.com/astrodsg/django-stock-up","Github Project StockUp"))
setattr(links,"github_user",Link("https://astrodsg.github.io","Dylan Gregersen"))

navbar_items = OrderedDict()
navbar_items["about"] = Link("/about","About")
navbar_items["login"] =  Link("/login","Log In")
# User profile

initial_cash = 10000