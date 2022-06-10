from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import CustomUser
from .forms import CustomuserCreationForm
# Create your views here.

# to create register or create custom user from web browser
class CustomUserCreateView(CreateView):
    form_class = CustomuserCreationForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy('home')
    