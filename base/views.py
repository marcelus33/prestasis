from datatableview.views import DatatableView
from django.contrib.auth.views import LoginView
from django.http import HttpResponseNotFound
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from base.forms import CuoteroForm
from base.models import Cuotero


class SiteLoginView(LoginView):
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


class CuoteroListView(DatatableView):
    template_name = 'cuotero/list.html'
    model = Cuotero
    context_object_name = "cuoteros"


class CuoteroListView2(ListView):
    template_name = 'cuotero/list.html'
    model = Cuotero
    context_object_name = "cuoteros"


class CuoteroDetailView(DetailView):
    template_name = 'cuotero/detail.html'
    model = Cuotero
    context_object_name = 'cuotero'
    pk_url_kwarg = 'cuotero_id'


class CuoteroCreateView(CreateView):
    template_name = 'cuotero/create.html'
    model = Cuotero
    success_url = reverse_lazy('cuotero.list')
    form_class = CuoteroForm


class CuoteroUpdateView(UpdateView):
    template_name = 'cuotero/update.html'
    model = Cuotero
    context_object_name = 'cuotero'
    pk_url_kwarg = 'cuotero_id'
    form_class = CuoteroForm

    def get_success_url(self):
        return reverse('cuotero.detail', kwargs={'cuotero_id': self.object.id})


class CuoteroDeleteView(DeleteView):
    template_name = 'cuotero/delete.html'
    model = Cuotero
    context_object_name = 'cuotero'
    pk_url_kwarg = 'cuotero_id'
    success_url = reverse_lazy('cuotero.list')
