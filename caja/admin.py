from django.contrib import admin
from django.contrib.admin import ModelAdmin

from caja.models import MovimientoCaja, ConceptoMovimiento


@admin.register(ConceptoMovimiento)
class ConceptoMovimientoAdmin(ModelAdmin):
    list_display = ['id', 'nombre']


@admin.register(MovimientoCaja)
class MovimientoCajaAdmin(ModelAdmin):
    list_display = ['id', 'fecha', 'descripcion', 'tipo', 'concepto', 'monto']

