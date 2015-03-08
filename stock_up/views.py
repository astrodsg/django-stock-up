from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView


class BaseTemplateView(TemplateView):

    def get_context_data(self,**kws):
        context = super().get_context_data(**kws)
        context['title'] = "StockUp"        
        context['navbar_title'] = "StockUp"
        context['navbar_items'] = [\
            ("Home","/"),
            ("Log In","/login"),
            ]
        return context

class HomeView(BaseTemplateView):

    template_name = "stock_up/index.html"

    def get_context_data(self,**kws):
        context = super().get_context_data(**kws)
        context['message'] = "hello world!"
        return context 

    # def get(self, request, *args, **kwargs):
    #     context = super().get_context_data(**kws)
    #     return HttpResponse('Hello, World!')


class LoginView(BaseTemplateView):

    template_name = "stock_up/login.html"

    def get_context_data(self,**kws):
        context = super().get_context_data(**kws)
        return context 
