from django.contrib.auth.views import LoginView
from django.http import HttpResponseNotFound
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from base.forms import CuoteroForm, ComisionMoraForm, VendedorForm, ClienteForm
from base.models import Cuotero, ComisionMora, Vendedor, Cliente


class SiteLoginView(LoginView):
    template_name = 'login.html'

    def get_success_url(self):
        user = self.request.user
        if not user.is_authenticated:
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


# CUOTERO
class CuoteroListView(ListView):
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


# COMISION Y MORA
class ComisionMoraListView(ListView):
    template_name = 'comisionmora/list.html'
    model = ComisionMora
    context_object_name = "comisiones_moras"


class ComisionMoraDetailView(DetailView):
    template_name = 'comisionmora/detail.html'
    model = ComisionMora
    context_object_name = 'comision_mora'
    pk_url_kwarg = 'comision_mora_id'


class ComisionMoraCreateView(CreateView):
    template_name = 'comisionmora/create.html'
    model = ComisionMora
    success_url = reverse_lazy('comision_mora.list')
    form_class = ComisionMoraForm


class ComisionMoraUpdateView(UpdateView):
    template_name = 'comisionmora/update.html'
    model = ComisionMora
    context_object_name = 'comision_mora'
    pk_url_kwarg = 'comision_mora_id'
    form_class = ComisionMoraForm

    def get_success_url(self):
        return reverse('comision_mora.detail', kwargs={'comision_mora_id': self.object.id})


class ComisionMoraDeleteView(DeleteView):
    template_name = 'comisionmora/delete.html'
    model = ComisionMora
    context_object_name = 'comision_mora'
    pk_url_kwarg = 'comision_mora_id'
    success_url = reverse_lazy('comision_mora.list')


# VENDEDOR
class VendedorListView(ListView):
    template_name = 'vendedor/list.html'
    model = Vendedor
    context_object_name = "vendedores"


class VendedorDetailView(DetailView):
    template_name = 'vendedor/detail.html'
    model = Vendedor
    context_object_name = 'vendedor'
    pk_url_kwarg = 'vendedor_id'


class VendedorCreateView(CreateView):
    template_name = 'vendedor/create.html'
    model = Vendedor
    success_url = reverse_lazy('vendedor.list')
    form_class = VendedorForm


class VendedorUpdateView(UpdateView):
    template_name = 'vendedor/update.html'
    model = Vendedor
    context_object_name = 'vendedor'
    pk_url_kwarg = 'vendedor_id'
    form_class = VendedorForm

    def get_success_url(self):
        return reverse('vendedor.detail', kwargs={'vendedor_id': self.object.id})


class VendedorDeleteView(DeleteView):
    template_name = 'vendedor/delete.html'
    model = Vendedor
    context_object_name = 'vendedor'
    pk_url_kwarg = 'vendedor_id'
    success_url = reverse_lazy('vendedor.list')


# CLIENTE
class ClienteListView(ListView):
    template_name = 'cliente/list.html'
    model = Cliente
    context_object_name = "clientes"


class ClienteDetailView(DetailView):
    template_name = 'cliente/detail.html'
    model = Cliente
    context_object_name = 'cliente'
    pk_url_kwarg = 'cliente_id'


class ClienteCreateView(CreateView):
    template_name = 'cliente/create.html'
    model = Cliente
    success_url = reverse_lazy('cliente.list')
    form_class = ClienteForm


class ClienteUpdateView(UpdateView):
    template_name = 'cliente/update.html'
    model = Cliente
    context_object_name = 'cliente'
    pk_url_kwarg = 'cliente_id'
    form_class = ClienteForm

    def get_success_url(self):
        return reverse('cliente.detail', kwargs={'cliente_id': self.object.id})


class ClienteDeleteView(DeleteView):
    template_name = 'cliente/delete.html'
    model = Cliente
    context_object_name = 'cliente'
    pk_url_kwarg = 'cliente_id'
    success_url = reverse_lazy('cliente.list')
