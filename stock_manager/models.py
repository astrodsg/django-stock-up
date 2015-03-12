"""
PURPOSE: Handles vote-boat models
DATE: Thu Jul 31 16:56:32 2014
"""
# ########################################################################### #
import datetime
from django.db import models
from django.utils import timezone
from django.utils.http import urlquote
from django.utils.translation import ugettext_lazy 
from django.core.mail import send_mail
from django.contrib.auth.models import User as DjangoUser

from stock_up.settings import site_variables

INITIAL_CASH = getattr(site_variables,'initial_cash',100)

# ########################################################################### #

class StockUpUser (DjangoUser):
    """ Create user accounts """

    display_name = models.CharField(max_length=80,help_text="Display Name")
    cash = models.FloatField(default=INITIAL_CASH)
    init_cash = models.FloatField(default=INITIAL_CASH)

    class Meta:
        ordering = ["username"]
    
    def get_absolute_url(self):
        return "/users/{}/".format(urlquote(self.email))

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = "{} {}".format(self.first_name,self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Returns the short name for the user."""
        return self.first_name

    def get_display_name (self):
        return self.display_name

    def email_user(self, subject, message, from_email=None):
        """ Sends an email to this User """
        if self.email is not None:
            send_mail(subject, message, from_email, [self.email])

class Portfoilo (models.Model):
    """ Create a set of ideas to vote on """

    stock_up_user_id = models.ForeignKey(StockUpUser,on_delete=models.CASCADE)

    # - - - - - - - - - - - - 
    name = models.CharField(max_length=100,help_text="Portfolio Name")
    description = models.CharField(max_length=200,help_text="Describe Portfolio",default=True)
    # - - - - - - - - - - - - 
    creation_date = models.DateTimeField(ugettext_lazy('created'), default=timezone.now)
    update_date = models.DateTimeField(ugettext_lazy('updated'), default=timezone.now)    

    class Meta:
        ordering = ['stock_up_user_id','name','creation_date']

class Stock (models.Model):
    """ Tracks User's Current Stocks """
    portfolio_id = models.ForeignKey(Portfoilo,on_delete=models.CASCADE)

    # - - - - - - - - - - - - 
    symbol = models.CharField(max_length=10,help_text="Stock Symbol")
    name = models.CharField(max_length=100,help_text="Stock Name")

    # - - - - - - - - - - - - 
    unit_price = models.FloatField()
    nstocks = models.IntegerField()
    creation_date = models.DateTimeField(ugettext_lazy('created'), default=timezone.now)

    def total_price (self):
        return self.unit_price*self.nstocks


