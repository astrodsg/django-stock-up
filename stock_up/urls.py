from django.conf import settings 
from django.conf.urls import patterns, include, url
from django.contrib import admin

from stock_up.views import HomeView
from stock_manager.views import SignupView,LoginView



from stock_manager.forms import StockUpAutheticationForm
LoginView.template_name = "stock_manager/login.html"
LoginView.form_class =  StockUpAutheticationForm
LoginView.success_url = "/profile/"

# ########################################################################### #

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='home'),    

    # signup/login/logout
    url(r'^login/',LoginView.as_view(),name="login"),
    url(r'^signup/', SignupView.as_view(template_name="stock_manager/signup.html"),name="signup"),    
    #url(r'^logout/$', logout_page),

    # Web portal.
    # (r'^portal/', include('portal.urls')),

    # Serve static content.
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': 'static'}),
)
    
if settings.DEBUG:
    urlpatterns.append(url(r'^admin/', include(admin.site.urls)))
