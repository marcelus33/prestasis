from django.contrib.auth.views import LoginView
from django.http import HttpResponseNotFound
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import TemplateView

from base import forms


class SiteLoginView(LoginView):
    form_class = forms.UserAuthenticationForm
    template_name = 'login.html'

    def get_success_url(self):
        user = self.request.user
        if not user.is_authenticated:
            # return self.handle_no_permission()
            return HttpResponseNotFound('<h1>Por favor ingrese al sistema</h1>')
        else:
            return reverse('home')
            # if user.groups.filter(name='Administrador').exists() or user.groups.filter(name='Operativo').exists():
            #     return reverse('dashboard')  # Dashboard Staff
            # elif self.request.GET.get('next'):
            #     return self.request.GET.get('next')
            # elif user.groups.filter(name='Proveedor').exists():
            #     return reverse('inicio')  # Dashboard Proveedor
            # elif user.groups.filter(name='Cliente').exists():
            #     return reverse('inicio')  # Inicio
        return HttpResponseNotFound('<h1>Error 404</h1>')


class HomeView(TemplateView):
    template_name = 'home.html'
