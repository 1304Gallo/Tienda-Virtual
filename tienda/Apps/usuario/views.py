from typing import Any

from django.contrib import messages
from django.http import HttpRequest, request
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView
from django.views.generic import FormView, RedirectView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from .form import CustomUserCreationForm
from django import forms
import logging


# Create your views here.

class LoginFormView(LoginView):
    template_name = 'registration/Login.html'

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if request.user.is_authenticated:
            return redirect('base')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Iniciar sesión'
        return super().get_context_data(**kwargs)


class LogoutRedirectView(RedirectView):
    pattern_name = 'login'

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        logout(request)
        return super().dispatch(request, *args, **kwargs)


class Forgot_PasswordView(PasswordResetView):
    template_name = "registration/forgot_password.html"


logger = logging.getLogger(__name__)

class CreateUserFormView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "registration/create_user.html"
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        logger.info(f'Datos del formulario: {form.cleaned_data}')

        user = form.save()
        messages.success(self.request, 'Usuario creado con éxito.')
        return super().form_valid(form)

    def form_invalid(self, form):
        return render(self.request, self.template_name, {'form': form})
