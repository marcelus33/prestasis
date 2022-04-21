from django.db import models

from base.models import Cliente, Vendedor, Cuotero


class Credito(models.Model):
    PENDIENTE = 1
    APROBADO = 2
    RECHAZADO = 3
    ESTADOS_CREDITO = (
        (PENDIENTE, "Pendiente"),
        (APROBADO, "Aprobado"),
        (RECHAZADO, "Rechazado"),
    )
    cliente = models.ForeignKey(Cliente, related_name="creditos", on_delete=models.PROTECT)
    vendedor = models.ForeignKey(Vendedor, related_name="creditos", on_delete=models.PROTECT)
    cuotero = models.ForeignKey(Cuotero, related_name="creditos", on_delete=models.PROTECT)
    estado = models.IntegerField(choices=ESTADOS_CREDITO, default=PENDIENTE)
    comentario = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        verbose_name = "Crédito"
        verbose_name_plural = "Créditos"


class Cuota(models.Model):
    credito = models.ForeignKey(Credito, related_name="cuotas", on_delete=models.CASCADE)
    fecha_vencimiento = models.DateField("Fecha de vencimiento")
    monto = models.PositiveIntegerField()

    class Meta:
        ordering = ('fecha_vencimiento',)
        verbose_name = "Cuota"
        verbose_name_plural = "Cuotas"


class Pago(models.Model):
    cuota = models.ForeignKey(Cuota, related_name="pagos", on_delete=models.PROTECT)
    fecha = models.DateField("Fecha de pago")
    monto = models.PositiveIntegerField()

    class Meta:
        ordering = ('cuota', 'fecha')
        verbose_name = "Pago de cuota"
        verbose_name_plural = "Pagos de cuotas"


class Comision(models.Model):
    NO_PAGADO = 1
    PAGADO = 2
    ESTADOS_COMISION = (
        (NO_PAGADO, "No pagado"),
        (PAGADO, "Pagado")
    )
    vendedor = models.ForeignKey(Vendedor, related_name="comisiones", on_delete=models.PROTECT)
    credito = models.OneToOneField(Credito, related_name="comision", on_delete=models.PROTECT)
    monto = models.PositiveIntegerField()
    estado = models.IntegerField(choices=ESTADOS_COMISION, default=NO_PAGADO)

    class Meta:
        verbose_name = "Comisión"
        verbose_name_plural = "Comisiones"

