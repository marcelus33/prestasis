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
            if user.is_superuser:
                return reverse('admin-home')  # TODO vista de superuser
            elif user.groups.filter(name='Admin').exists():
                return reverse('admin-home')
            elif user.groups.filter(name='Agente').exists():
                return reverse('home')
        return HttpResponseNotFound('<h1>No se ha encontrado página solicitada</h1>')


class HomeView(TemplateView):
    template_name = 'home.html'


class DashboardView(TemplateView):
    template_name = 'dashboard.html'
