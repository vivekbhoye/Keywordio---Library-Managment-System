from django import forms 
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

from .models import CustomUser

# to create custom user with email as login 
class CustomuserCreationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = CustomUser
        fields =['email','username','password1','password2']
