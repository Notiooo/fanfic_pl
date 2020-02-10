from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views

from .forms import CustomUserCreationForm, CustomUserLoginForm

# Create your views here.


class RegisterView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/register.html'


class CustomLoginView(auth_views.LoginView):
    authentication_form = CustomUserLoginForm