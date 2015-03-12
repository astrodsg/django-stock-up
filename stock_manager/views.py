from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView,View
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


from class_based_auth_views.views import LoginView as BaseLoginView

from stock_up.views import include_base_context

from stock_manager.forms import StockUpAutheticationForm, StockUpUserCreationForm


class UserView (object):

    def get(self,request):
        """ For retrieving a specific user's home page """
        pass 

    def post(self,request):
        """ For either creating or logging in a user """
        pass 

    def delete(self,request):
        """ delete a user """
        pass 

class LoginView(BaseLoginView):
    
    @include_base_context
    def get_context_data(self,**kws):
        return super().get_context_data(**kws)

LoginView.form_class = StockUpAutheticationForm


class SignupView(TemplateView):

    template_name = "stock_up/signup.html"

    @include_base_context
    def get_context_data(self,**kws):
        context = super().get_context_data(**kws)
        return context 


    def form_class (self):
        if 'login' in self.template_name:
            Form = LoginForm
        else:
            Form = StockUpUserCreationForm
        return Form

    @login_required(login_url='/login/')
    def get(self, request):
        Form = self.form_class()
        context = self.get_context_data() 
        context['form'] = Form()
        #import pdb;pdb.set_trace()
        return render(request,self.template_name,context)

    def post(self, request): 
        Form = self.form_class()       
        context = self.get_context_data()   
        if request is None:
            context['form'] = Form()
        else:
            form = Form(request.POST)
            if form.is_valid():
                user = form.save()

            #return HttpResponseRedirect(author.get_absolute_url())                

        import pdb;pdb.set_trace()
        return render(request,self.template_name,context)


