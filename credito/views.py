from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from base.forms import ClienteForm
from base.mixins import AdminMixin
from base.models import Cliente
from credito.forms import CreditoForm, CreditoVendedorForm, PagoForm, ComisionForm, ClienteModalForm
from credito.models import Credito, Pago, Comision


class ClienteCreateView(LoginRequiredMixin, CreateView):
    template_name = 'credito/cliente_modal.html'
    model = Cliente
    success_url = reverse_lazy('credito.create')
    form_class = ClienteModalForm

    def form_valid(self, form):
        if form.is_valid():
            super(ClienteCreateView, self).form_valid(form)
            data = {"success": True}
            return JsonResponse(data)
        return super(ClienteCreateView, self).form_valid(form)


class CreditoListView(ListView):
    template_name = 'credito/list.html'
    model = Credito
    context_object_name = "creditos"

    def get_queryset(self):
        user = self.request.user
        queryset = super().get_queryset()
        if user.groups.filter(name="Agente").exists():
            queryset = queryset.filter(vendedor__usuario=user)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(CreditoListView, self).get_context_data(**kwargs)
        context["activo"] = "todos"
        return context


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

    def get_form_kwargs(self):
        kwargs = super(CreditoCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_form_class(self):
        user = self.request.user
        if user.groups.filter(name="Agente").exists():
            return CreditoVendedorForm
        return CreditoForm


class CreditoUpdateView(UpdateView):
    template_name = 'credito/update.html'
    model = Credito
    context_object_name = 'credito'
    pk_url_kwarg = 'credito_id'
    form_class = CreditoForm

    def get_success_url(self):
        return reverse('credito.detail', kwargs={'credito_id': self.object.id})


class CreditoDeleteView(DeleteView, AdminMixin):
    template_name = 'credito/delete.html'
    model = Credito
    context_object_name = 'credito'
    pk_url_kwarg = 'credito_id'
    success_url = reverse_lazy('credito.list')


class CreditoPendienteListView(CreditoListView):
    template_name = 'credito/list.html'
    model = Credito
    context_object_name = "creditos"

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(estado=Credito.PENDIENTE)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(CreditoListView, self).get_context_data(**kwargs)
        context["activo"] = "pendientes"
        return context


class CreditoAprobadoListView(CreditoListView):
    template_name = 'credito/list.html'
    model = Credito
    context_object_name = "creditos"

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(estado=Credito.APROBADO)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(CreditoListView, self).get_context_data(**kwargs)
        context["activo"] = "aprobados"
        return context


class CreditoDesembolsadoListView(CreditoListView):
    template_name = 'credito/list.html'
    model = Credito
    context_object_name = "creditos"

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(estado=Credito.DESEMBOLSADO)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(CreditoListView, self).get_context_data(**kwargs)
        context["activo"] = "desembolsados"
        return context


class CreditoRechazadoListView(CreditoListView):
    template_name = 'credito/list.html'
    model = Credito
    context_object_name = "creditos"

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(estado=Credito.RECHAZADO)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(CreditoListView, self).get_context_data(**kwargs)
        context["activo"] = "rechazados"
        return context


# PAGOS
class PagoListView(ListView, AdminMixin):
    template_name = 'pago/list.html'
    model = Pago
    context_object_name = "comisiones_moras"


class PagoDetailView(DetailView, AdminMixin):
    template_name = 'pago/detail.html'
    model = Pago
    context_object_name = 'pago'
    pk_url_kwarg = 'pago_id'


class PagoCreateView(CreateView, AdminMixin):
    template_name = 'pago/create.html'
    model = Pago
    success_url = reverse_lazy('pago.list')
    form_class = PagoForm


class PagoUpdateView(UpdateView, AdminMixin):
    template_name = 'pago/update.html'
    model = Pago
    context_object_name = 'pago'
    pk_url_kwarg = 'pago_id'
    form_class = PagoForm

    def get_success_url(self):
        return reverse('pago.detail', kwargs={'pago_id': self.object.id})


class PagoDeleteView(DeleteView, AdminMixin):
    template_name = 'pago/delete.html'
    model = Pago
    context_object_name = 'pago'
    pk_url_kwarg = 'pago_id'
    success_url = reverse_lazy('pago.list')


#  COMISION (Pago de)
class ComisionListView(ListView, AdminMixin):
    template_name = 'comision/list.html'
    model = Comision
    context_object_name = "comisiones"


class ComisionDetailView(DetailView, AdminMixin):
    template_name = 'comision/detail.html'
    model = Comision
    context_object_name = 'comision'
    pk_url_kwarg = 'comision_id'


class ComisionCreateView(CreateView, AdminMixin):
    template_name = 'comision/create.html'
    model = Comision
    success_url = reverse_lazy('comision.list')
    form_class = ComisionForm


class ComisionUpdateView(UpdateView, AdminMixin):
    template_name = 'comision/update.html'
    model = Comision
    context_object_name = 'comision'
    pk_url_kwarg = 'comision_id'
    form_class = ComisionForm

    def get_success_url(self):
        return reverse('comision.detail', kwargs={'comision_id': self.object.id})


class ComisionDeleteView(DeleteView, AdminMixin):
    template_name = 'comision/delete.html'
    model = Comision
    context_object_name = 'comision'
    pk_url_kwarg = 'comision_id'
    success_url = reverse_lazy('comision.list')


