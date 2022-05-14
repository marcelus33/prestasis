from django.contrib.auth.models import User
from django.db import models


class Cuotero(models.Model):
    SEMANAL = 7
    QUINCENAL = 14
    MENSUAL = 30
    TIPOS_PLAZOS = (
        (SEMANAL, "Semanal"),
        (8, "Semanal"),
        (QUINCENAL, "Quincenal"),
        (15, "Quincenal"),
        (MENSUAL, "Mensual"),
    )
    monto = models.PositiveIntegerField(verbose_name="Monto del préstamo")
    cuotas = models.PositiveIntegerField(verbose_name="Cantidad de cuotas")
    tipo_plazo = models.IntegerField(verbose_name="Tipo de plazo", choices=TIPOS_PLAZOS)
    pagare = models.PositiveIntegerField(verbose_name="Pagaré")

    class Meta:
        unique_together = [['monto', 'cuotas', 'tipo_plazo', 'pagare']]
        ordering = ['monto', 'pagare']
        verbose_name = "Cuotero"
        verbose_name_plural = "Cuotas"

    def __str__(self):
        monto = "{:,}".format(self.monto).replace(",", ".")
        return "Monto: Gs.{} - Cuotas: {} - {}".format(monto, self.cuotas, self.get_tipo_plazo_display())

    def get_interes(self):
        return self.pagare - self.monto

    def get_monto_cuota(self):
        return int(self.pagare / self.cuotas) if self.cuotas else 0


class ComisionMora(models.Model):
    monto = models.PositiveIntegerField()
    mora_por_dia = models.PositiveIntegerField()
    comision = models.PositiveIntegerField()

    class Meta:
        ordering = ('monto',)
        verbose_name = "Comisión y Mora"
        verbose_name_plural = "Comisiones y Moras"

    def __str__(self):
        return "{} - {} - {}".format(self.monto, self.mora_por_dia, self.comision)


class Usuario(User):
    class Meta:
        proxy = True

    def __str__(self):
        return "{} - {}".format(self.username, self.email if self.email else "(sin correo)")


class Vendedor(models.Model):
    nombre = models.CharField(max_length=256)
    usuario = models.OneToOneField(Usuario, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ('nombre',)
        verbose_name = "Vendedor"
        verbose_name_plural = "Vendedores"

    def __str__(self):
        return "{}".format(self.nombre)


class TipoDocumento(models.Model):
    nombre = models.CharField("Tipo de documento", max_length=32)

    class Meta:
        ordering = ('nombre',)
        verbose_name = "Tipo de documento"
        verbose_name_plural = "Tipos de documento"

    def __str__(self):
        return self.nombre


class Cliente(models.Model):
    nombre = models.CharField(max_length=256)
    tipo_documento = models.ForeignKey(TipoDocumento, related_name="clientes", on_delete=models.PROTECT, null=True,
                                       blank=False)
    ci = models.CharField(max_length=16, blank=True, null=True)
    direccion = models.CharField(max_length=128, blank=True, null=True)
    telefono = models.CharField(max_length=128, blank=True, null=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)

    class Meta:
        unique_together = [['tipo_documento', 'ci']]
        ordering = ('nombre',)
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return "{}".format(self.nombre)

