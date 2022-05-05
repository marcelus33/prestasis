from django.contrib.auth.models import User
from django.db import models


class Cuotero(models.Model):
    SEMANAL = 8
    QUINCENAL = 15
    MENSUAL = 30
    TIPOS_PLAZOS = (
        (SEMANAL, "Semanal"),
        (QUINCENAL, "Quincenal"),
        (MENSUAL, "Mensual"),
    )
    monto = models.PositiveIntegerField()
    cuotas = models.PositiveIntegerField()
    tipo_plazo = models.IntegerField(verbose_name="Tipo de plazo", choices=TIPOS_PLAZOS)
    pagare = models.PositiveIntegerField(verbose_name="Pagaré")

    class Meta:
        ordering = ('monto',)
        verbose_name = "Cuotero"
        verbose_name_plural = "Cuotas"

    def __str__(self):
        monto = "{:,}".format(self.monto).replace(",", ".")
        return "Monto: Gs.{} - Cuotas: {} - {}".format(monto, self.cuotas, self.get_tipo_plazo_display())

    def get_interes(self):
        return self.pagare - self.monto

    def get_monto_cuota(self):
        return self.pagare / self.cuotas if self.cuotas else 0


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
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    usuario = models.OneToOneField(Usuario, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ('apellido',)
        verbose_name = "Vendedor"
        verbose_name_plural = "Vendedores"

    def __str__(self):
        return "{}".format(self.get_nombre_completo())

    def get_nombre_completo(self):
        return "{}, {}".format(self.apellido, self.nombre)


class TipoDocumento(models.Model):
    nombre = models.CharField("Tipo de documento", max_length=32)

    class Meta:
        ordering = ('nombre',)
        verbose_name = "Tipo de documento"
        verbose_name_plural = "Tipos de documento"

    def __str__(self):
        return self.nombre


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    tipo_documento = models.ForeignKey(TipoDocumento, related_name="clientes", on_delete=models.PROTECT, null=True,
                                       blank=False)
    ci = models.CharField(max_length=16, blank=True, null=True)
    direccion = models.CharField(max_length=128, blank=True, null=True)
    telefono = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        ordering = ('apellido',)
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return "{} - {}".format(self.get_nombre_completo(), self.ci if self.ci else "(Sin CI)")

    def get_nombre_completo(self):
        return "{}, {}".format(self.apellido, self.nombre)
