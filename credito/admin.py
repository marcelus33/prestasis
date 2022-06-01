from django.contrib import admin
from django.contrib.admin import ModelAdmin

from credito.models import Credito, Pago, Cuota, Comision


@admin.register(Credito)
class ClienteAdmin(ModelAdmin):
    list_display = ['id', 'fecha_alta', 'numero', 'cliente', 'vendedor']


@admin.register(Pago)
class PagoAdmin(ModelAdmin):
    list_display = ['id', 'cuota', 'fecha', 'monto']


@admin.register(Cuota)
class CuotaAdmin(ModelAdmin):
    list_display = ['id', 'credito', 'fecha_vencimiento', 'monto']


@admin.register(Comision)
class ComisionAdmin(ModelAdmin):
    list_display = ['id', 'credito', 'vendedor', 'estado']
