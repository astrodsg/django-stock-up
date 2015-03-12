from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from stock_manager.models import StockUpUser

class StockUpAutheticationForm(AuthenticationForm):

    def __init__ (self,*args,**kwargs):
        super().__init__(*args, **kwargs)        

        UserModel = StockUpUser
        self.username_field = UserModel._meta.get_field(UserModel.USERNAME_FIELD)
        if self.fields['username'].label is None:
            self.fields['username'].label = capfirst(self.username_field.verbose_name)



class StockUpUserCreationForm(UserCreationForm):

    class Meta:
        modle = StockUpUser
        fields = ('username','email','display_name')


class LoginForm(forms.ModelForm):

    class Meta:
        model = StockUpUser 
        fields = ['username','password']
        widgets = {\
            'password':forms.PasswordInput(),
            }
        # TODO: or email login

