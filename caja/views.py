from django.shortcuts import render

# VENDEDOR
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from base.mixins import AdminMixin
from caja.forms import MovimientoCajaForm
from caja.models import MovimientoCaja


class MovimientoCajaListView(ListView, AdminMixin):
    template_name = 'movimiento_caja/list.html'
    model = MovimientoCaja
    context_object_name = "movimientos_caja"


class MovimientoCajaDetailView(DetailView, AdminMixin):
    template_name = 'movimiento_caja/detail.html'
    model = MovimientoCaja
    context_object_name = 'movimiento_caja'
    pk_url_kwarg = 'movimiento_caja_id'


class MovimientoCajaCreateView(CreateView, AdminMixin):
    template_name = 'movimiento_caja/create.html'
    model = MovimientoCaja
    success_url = reverse_lazy('movimiento_caja.list')
    form_class = MovimientoCajaForm


class MovimientoCajaUpdateView(UpdateView, AdminMixin):
    template_name = 'movimiento_caja/update.html'
    model = MovimientoCaja
    context_object_name = 'movimiento_caja'
    pk_url_kwarg = 'movimiento_caja_id'
    form_class = MovimientoCajaForm

    def get_success_url(self):
        return reverse('movimiento_caja.detail', kwargs={'movimiento_caja_id': self.object.id})


class MovimientoCajaDeleteView(DeleteView, AdminMixin):
    template_name = 'movimiento_caja/delete.html'
    model = MovimientoCaja
    context_object_name = 'movimiento_caja'
    pk_url_kwarg = 'movimiento_caja_id'
    success_url = reverse_lazy('movimiento_caja.list')

