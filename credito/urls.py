# from django.conf.urls import url
from django.urls import path

import credito.views

urlpatterns = [
    path('credito/', credito.views.CreditoListView.as_view(), name='credito.list'),
    path('credito/<int:credito_id>/', credito.views.CreditoDetailView.as_view(), name='credito.detail'),
    path('credito/crear/', credito.views.CreditoCreateView.as_view(), name='credito.create'),
    path('credito/<int:credito_id>/editar/', credito.views.CreditoUpdateView.as_view(), name='credito.update'),
    path('credito/<int:credito_id>/eliminar/', credito.views.CreditoDeleteView.as_view(), name='credito.delete'),
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
]
