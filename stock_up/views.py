from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.contrib.auth import authenticate, login

from stock_up.settings import site_variables

def include_base_context (func):
    """ 
    Add context used within the base.html template
    """
    def get_context_data_wrapper (*args,**kwargs):
        context = func(*args,**kwargs)
        # - - - - - - - - - - - - 
        context['title'] = site_variables.title
        context['navbar_title'] = site_variables.title
        context['navbar_items'] = site_variables.navbar_items
        context['links'] = site_variables.links
        # - - - - - - - - - - - - 
        return context
    get_context_data_wrapper.__doc__ = func.__doc__
    return get_context_data_wrapper

class HomeView(TemplateView):
    template_name = "stock_up/index.html"

    @include_base_context
    def get_context_data(self,**kws):
        return super().get_context_data(**kws)

