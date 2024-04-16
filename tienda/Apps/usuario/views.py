from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView
from django.views.generic import FormView, RedirectView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout


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