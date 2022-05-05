from django.db import models

from credito.models import Pago


class ConceptoMovimiento(models.Model):
    nombre = models.CharField("Concepto", max_length=64)

    class Meta:
        ordering = ('nombre',)
        verbose_name = "Concepto de movimiento"
        verbose_name_plural = "Conceptos de movimientos"

    def __str__(self):
        return self.nombre


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
    concepto = models.ForeignKey(ConceptoMovimiento, related_name="movimientos", on_delete=models.PROTECT, null=True,
                                 blank=False)
    monto = models.PositiveIntegerField()
    saldo = models.IntegerField()

    class Meta:
        ordering = ('fecha',)
        verbose_name = "Movimiento de caja"
        verbose_name_plural = "Movimientos de caja"

    def __str__(self):
        return "{} {} {}".format(self.fecha, self.tipo, self.monto)
