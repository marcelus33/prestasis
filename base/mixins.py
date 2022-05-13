from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, AccessMixin
from django.shortcuts import get_object_or_404, redirect
from django.views import View

from credito.models import Credito


class AdminMixin(LoginRequiredMixin, View):
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return super(LoginRequiredMixin, self).handle_no_permission()
        if not self.request.user.groups.filter(name="Admin").exists():
            messages.warning(self.request, 'No tiene los permisos necesarios.')
            return redirect("home")
        return super(AdminMixin, self).dispatch(request, *args, **kwargs)


class VendedorCreditoMixin(LoginRequiredMixin, View):
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return super(LoginRequiredMixin, self).handle_no_permission()
        if self.request.user.groups.filter(name="Agente").exists():
            credito_id = kwargs.get('credito_id')
            credito = get_object_or_404(Credito, pk=credito_id)
            user = self.request.user
            if not credito.vendedor.usuario == user:
                messages.error(self.request, 'No tiene los permisos necesarios.')
                return redirect('credito.list')
        return super(VendedorCreditoMixin, self).dispatch(request, *args, **kwargs)


class VendedorCreditoEditarMixin(LoginRequiredMixin, View):
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return super(LoginRequiredMixin, self).handle_no_permission()
        if self.request.user.groups.filter(name="Agente").exists():
            credito_id = kwargs.get('credito_id')
            credito = get_object_or_404(Credito, pk=credito_id)
            user = self.request.user
            if not credito.vendedor.usuario == user:
                messages.error(self.request, 'No tiene los permisos necesarios.')
                return redirect('credito.list')
            if credito.estado != Credito.PENDIENTE:
                messages.error(self.request, 'No se puede editar un Crédito ya aprobado.')
                return redirect('credito.list')
        return super(VendedorCreditoEditarMixin, self).dispatch(request, *args, **kwargs)

