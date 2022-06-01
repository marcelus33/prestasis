from django.contrib import admin
from django.contrib.admin import ModelAdmin

from base.models import Usuario, Vendedor, Cliente, TipoDocumento, Cuotero


@admin.register(Usuario)
class UsuarioAdmin(ModelAdmin):
    list_display = ['id', 'username']


@admin.register(Vendedor)
class VendedorAdmin(ModelAdmin):
    list_display = ['id', 'nombre']


@admin.register(Cliente)
class ClienteAdmin(ModelAdmin):
    list_display = ['id', 'nombre']


@admin.register(Cuotero)
class CuoteroAdmin(ModelAdmin):
    list_display = ['id', 'monto', 'cuotas', 'tipo_plazo']


@admin.register(TipoDocumento)
class TipoDocumentoAdmin(ModelAdmin):
    list_display = ['id', 'nombre']
