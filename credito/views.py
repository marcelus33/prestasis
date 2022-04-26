from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from credito.forms import CreditoForm, PagoForm, ComisionForm
from credito.models import Credito, Pago, Comision


class CreditoListView(ListView):
    template_name = 'credito/list.html'
    model = Credito
    context_object_name = "creditos"


class CreditoDetailView(DetailView):
    template_name = 'credito/detail.html'
    model = Credito
    context_object_name = 'credito'
    pk_url_kwarg = 'credito_id'


class CreditoCreateView(CreateView):
    template_name = 'credito/create.html'
    model = Credito
    success_url = reverse_lazy('credito.list')
    form_class = CreditoForm


class CreditoUpdateView(UpdateView):
    template_name = 'credito/update.html'
    model = Credito
    context_object_name = 'credito'
    pk_url_kwarg = 'credito_id'
    form_class = CreditoForm

    def get_success_url(self):
        return reverse('credito.detail', kwargs={'credito_id': self.object.id})


class CreditoDeleteView(DeleteView):
    template_name = 'credito/delete.html'
    model = Credito
    context_object_name = 'credito'
    pk_url_kwarg = 'credito_id'
    success_url = reverse_lazy('credito.list')


# PAGOS
class PagoListView(ListView):
    template_name = 'pago/list.html'
    model = Pago
    context_object_name = "comisiones_moras"


class PagoDetailView(DetailView):
    template_name = 'pago/detail.html'
    model = Pago
    context_object_name = 'pago'
    pk_url_kwarg = 'pago_id'


class PagoCreateView(CreateView):
    template_name = 'pago/create.html'
    model = Pago
    success_url = reverse_lazy('pago.list')
    form_class = PagoForm


class PagoUpdateView(UpdateView):
    template_name = 'pago/update.html'
    model = Pago
    context_object_name = 'pago'
    pk_url_kwarg = 'pago_id'
    form_class = PagoForm

    def get_success_url(self):
        return reverse('pago.detail', kwargs={'pago_id': self.object.id})


class PagoDeleteView(DeleteView):
    template_name = 'pago/delete.html'
    model = Pago
    context_object_name = 'pago'
    pk_url_kwarg = 'pago_id'
    success_url = reverse_lazy('pago.list')


#  COMISION (Pago de)
class ComisionListView(ListView):
    template_name = 'comision/list.html'
    model = Comision
    context_object_name = "comisiones"


class ComisionDetailView(DetailView):
    template_name = 'comision/detail.html'
    model = Comision
    context_object_name = 'comision'
    pk_url_kwarg = 'comision_id'


class ComisionCreateView(CreateView):
    template_name = 'comision/create.html'
    model = Comision
    success_url = reverse_lazy('comision.list')
    form_class = ComisionForm


class ComisionUpdateView(UpdateView):
    template_name = 'comision/update.html'
    model = Comision
    context_object_name = 'comision'
    pk_url_kwarg = 'comision_id'
    form_class = ComisionForm

    def get_success_url(self):
        return reverse('comision.detail', kwargs={'comision_id': self.object.id})


class ComisionDeleteView(DeleteView):
    template_name = 'comision/delete.html'
    model = Comision
    context_object_name = 'comision'
    pk_url_kwarg = 'comision_id'
    success_url = reverse_lazy('comision.list')


