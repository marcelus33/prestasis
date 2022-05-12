from datetime import timedelta

from django.db import transaction

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
