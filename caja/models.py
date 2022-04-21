from django.db import models

from credito.models import Pago


class MovimientoCaja(models.Model):
    INGRESO = 1
    EGRESO = 2
    TIPOS_MOVIMIENTOS = (
        (INGRESO, "Ingreso"),
        (EGRESO, "Egreso"),
    )
    fecha = models.DateField()
    pago_cuota = models.OneToOneField(Pago, related_name="movimiento_caja", on_delete=models.CASCADE, null=True,
                                      blank=True)
    descripcion = models.CharField(max_length=128)
    tipo = models.IntegerField(choices=TIPOS_MOVIMIENTOS)
    monto = models.PositiveIntegerField()
    saldo = models.IntegerField()
