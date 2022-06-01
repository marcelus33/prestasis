from datetime import timedelta

from django.db import transaction

from caja.models import MovimientoCaja, ConceptoMovimiento
from credito.models import Cuota


def crear_cuotas(credito):
    exito = True
    cuotero = credito.cuotero
    pagare = cuotero.pagare
    cuotas = cuotero.cuotas
    plazo = cuotero.tipo_plazo
    fecha_inicial = credito.fecha_desembolso
    monto_cuotas = pagare / cuotas
    with transaction.atomic():
        try:
            for c in range(1, cuotas + 1):
                fecha_vencimiento = fecha_inicial + timedelta(days=(plazo * c))
                Cuota.objects.create(credito=credito, monto=monto_cuotas, fecha_vencimiento=fecha_vencimiento)
        except Exception as e:
            exito = False
    return exito


def crear_movimiento_desembolso(credito):
    concepto = ConceptoMovimiento.objects.filter(nombre__icontains='DESEMBOLSO').first()
    MovimientoCaja.objects.create(
        fecha=credito.fecha_alta,
        descripcion="DESEMBOLSO",
        tipo=MovimientoCaja.EGRESO,
        concepto=concepto,
        monto=credito.monto
    )
