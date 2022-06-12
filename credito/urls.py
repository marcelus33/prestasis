# from django.conf.urls import url
from django.urls import path

import credito.views

urlpatterns = [
    path('credito/', credito.views.CreditoListView.as_view(), name='credito.list'),
    path('credito/<int:credito_id>/', credito.views.CreditoDetailView.as_view(), name='credito.detail'),
    path('credito/crear/', credito.views.CreditoCreateView.as_view(), name='credito.create'),
    path('credito/<int:credito_id>/editar/', credito.views.CreditoUpdateView.as_view(), name='credito.update'),
    path('credito/<int:credito_id>/eliminar/', credito.views.CreditoDeleteView.as_view(), name='credito.delete'),
    path('credito/pendientes/', credito.views.CreditoPendienteListView.as_view(), name='credito_pendientes.list'),
    path('credito/aprobados/', credito.views.CreditoAprobadoListView.as_view(), name='credito_aprobados.list'),
    path('credito/desembolsados/', credito.views.CreditoDesembolsadoListView.as_view(),
         name='credito_desembolsados.list'),
    path('credito/rechazados/', credito.views.CreditoRechazadoListView.as_view(), name='credito_rechazados.list'),
    path('credito/<int:credito_id>/desembolsar/', credito.views.CreditoDesembolsarView.as_view(),
         name='credito.desembolsar'),
    # PAGOS
    path('pago/', credito.views.PagoListView.as_view(), name='pago.list'),
    path('pago/<int:pago_id>/', credito.views.PagoDetailView.as_view(), name='pago.detail'),
    path('pago/crear/', credito.views.PagoCreateView.as_view(), name='pago.create'),
    path('pago/<int:pago_id>/editar/', credito.views.PagoUpdateView.as_view(), name='pago.update'),
    path('pago/<int:pago_id>/eliminar/', credito.views.PagoDeleteView.as_view(), name='pago.delete'),
    # COMISION
    path('comision/', credito.views.ComisionListView.as_view(), name='comision.list'),
    path('comision/<int:comision_id>/', credito.views.ComisionDetailView.as_view(), name='comision.detail'),
    path('comision/crear/', credito.views.ComisionCreateView.as_view(), name='comision.create'),
    path('comision/<int:comision_id>/editar/', credito.views.ComisionUpdateView.as_view(), name='comision.update'),
    path('comision/<int:comision_id>/eliminar/', credito.views.ComisionDeleteView.as_view(), name='comision.delete'),
    # AJAX
    path('cliente/crear/', credito.views.ClienteCreateView.as_view(), name='cliente_ajax.create'),
    path('credito/procesar/', credito.views.CreditoProcesarView.as_view(), name='credito_ajax.procesar'),
    path('cliente/cuotas/', credito.views.ClienteCuotasView.as_view(), name='cliente_ajax.get_cuotas'),
]
