from django.contrib.auth.views import LogoutView
from django.urls import path

import base.views

urlpatterns = [
    path('', base.views.SiteLoginView.as_view(), name='login'),
    path('login/', base.views.SiteLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('inicio/', base.views.HomeView.as_view(), name='home'),
    path('dashboard/', base.views.DashboardView.as_view(), name='admin-home'),
    # Cuotero
    path('cuotero/', base.views.CuoteroListView.as_view(), name='cuotero.list'),
    path('cuotero/<int:cuotero_id>/', base.views.CuoteroDetailView.as_view(), name='cuotero.detail'),
    path('cuotero/crear/', base.views.CuoteroCreateView.as_view(), name='cuotero.create'),
    path('cuotero/<int:cuotero_id>/editar/', base.views.CuoteroUpdateView.as_view(), name='cuotero.update'),
    path('cuotero/<int:cuotero_id>/eliminar/', base.views.CuoteroDeleteView.as_view(), name='cuotero.delete'),
    # Comisión y Mora
    path('comision-mora/', base.views.ComisionMoraListView.as_view(), name='comision_mora.list'),
    path('comision-mora/<int:comision_mora_id>/', base.views.ComisionMoraDetailView.as_view(),
         name='comision_mora.detail'),
    path('comision-mora/crear/', base.views.ComisionMoraCreateView.as_view(), name='comision_mora.create'),
    path('comision-mora/<int:comision_mora_id>/editar/', base.views.ComisionMoraUpdateView.as_view(),
         name='comision_mora.update'),
    path('comision-mora/<int:comision_mora_id>/eliminar/', base.views.ComisionMoraDeleteView.as_view(),
         name='comision_mora.delete'),
    # Vendedor
    path('vendedor/', base.views.VendedorListView.as_view(), name='vendedor.list'),
    path('vendedor/<int:vendedor_id>/', base.views.VendedorDetailView.as_view(), name='vendedor.detail'),
    path('vendedor/crear/', base.views.VendedorCreateView.as_view(), name='vendedor.create'),
    path('vendedor/<int:vendedor_id>/editar/', base.views.VendedorUpdateView.as_view(), name='vendedor.update'),
    path('vendedor/<int:vendedor_id>/eliminar/', base.views.VendedorDeleteView.as_view(), name='vendedor.delete'),
    # Cliente
    path('cliente/', base.views.ClienteListView.as_view(), name='cliente.list'),
    path('cliente/<int:cliente_id>/', base.views.ClienteDetailView.as_view(), name='cliente.detail'),
    path('cliente/crear/', base.views.ClienteCreateView.as_view(), name='cliente.create'),
    path('cliente/<int:cliente_id>/editar/', base.views.ClienteUpdateView.as_view(), name='cliente.update'),
    path('cliente/<int:cliente_id>/eliminar/', base.views.ClienteDeleteView.as_view(), name='cliente.delete'),
    # Usuario
    path('usuario/', base.views.UsuarioListView.as_view(), name='usuario.list'),
    path('usuario/<int:usuario_id>/', base.views.UsuarioDetailView.as_view(), name='usuario.detail'),
    path('usuario/crear/', base.views.UsuarioCreateView.as_view(), name='usuario.create'),
    path('usuario/<int:usuario_id>/editar/', base.views.UsuarioUpdateView.as_view(), name='usuario.update'),
    path('usuario/<int:usuario_id>/eliminar/', base.views.UsuarioDeleteView.as_view(), name='usuario.delete'),
    # TipoDocumento
    path('tipo-documento/', base.views.TipoDocumentoListView.as_view(), name='tipo_documento.list'),
    path('tipo-documento/<int:tipo_documento_id>/', base.views.TipoDocumentoDetailView.as_view(),
         name='tipo_documento.detail'),
    path('tipo-documento/crear/', base.views.TipoDocumentoCreateView.as_view(), name='tipo_documento.create'),
    path('tipo-documento/<int:tipo_documento_id>/editar/', base.views.TipoDocumentoUpdateView.as_view(),
         name='tipo_documento.update'),
    path('tipo-documento/<int:tipo_documento_id>/eliminar/', base.views.TipoDocumentoDeleteView.as_view(),
         name='tipo_documento.delete'),

]
