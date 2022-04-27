from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, AccessMixin
from django.views import View


class AdminMixin(LoginRequiredMixin, View):
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return super(LoginRequiredMixin, self).handle_no_permission()
        if not self.request.user.groups.filter(name="Admin").exists():
            messages.error(self.request, 'No tiene los permisos necesarios.')
            return super(LoginRequiredMixin, self).handle_no_permission()
        return super(AdminMixin, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(AdminMixin, self).get_context_data(*args, **kwargs)
        return context

