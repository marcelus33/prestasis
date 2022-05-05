# from django.conf.urls import url
from django.urls import path

import caja.views

urlpatterns = [
    path('caja/', caja.views.MovimientoCajaListView.as_view(), name='movimiento_caja.list'),
    path('caja/<int:movimiento_caja_id>/', caja.views.MovimientoCajaDetailView.as_view(),
         name='movimiento_caja.detail'),
    path('caja/crear/', caja.views.MovimientoCajaCreateView.as_view(), name='movimiento_caja.create'),
    path('caja/<int:movimiento_caja_id>/editar/', caja.views.MovimientoCajaUpdateView.as_view(),
         name='movimiento_caja.update'),
    path('caja/<int:movimiento_caja_id>/eliminar/', caja.views.MovimientoCajaDeleteView.as_view(),
         name='movimiento_caja.delete'),
    # CONCEPTO MOVIMIENTO
    path('concepto-movimiento/', caja.views.ConceptoMovimientoListView.as_view(), name='concepto_movimiento.list'),
    path('concepto-movimiento/<int:concepto_movimiento_id>/', caja.views.ConceptoMovimientoDetailView.as_view(),
         name='concepto_movimiento.detail'),
    path('concepto-movimiento/crear/', caja.views.ConceptoMovimientoCreateView.as_view(),
         name='concepto_movimiento.create'),
    path('concepto-movimiento/<int:concepto_movimiento_id>/editar/', caja.views.ConceptoMovimientoUpdateView.as_view(),
         name='concepto_movimiento.update'),
    path('concepto-movimiento/<int:concepto_movimiento_id>/eliminar/',
         caja.views.ConceptoMovimientoDeleteView.as_view(),
         name='concepto_movimiento.delete'),
]
