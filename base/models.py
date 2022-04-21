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
    tipo_plazo = models.IntegerField(choices=TIPOS_PLAZOS)
    pagare = models.PositiveIntegerField()

    class Meta:
        ordering = ('monto',)
        verbose_name = "Cuotero"
        verbose_name_plural = "Cuotas"

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


class Vendedor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)

    class Meta:
        ordering = ('apellido',)
        verbose_name = "Vendedor"
        verbose_name_plural = "Vendedores"

    def get_nombre_completo(self):
        return "{}, {}".format(self.apellido, self.nombre)


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    ci = models.CharField(max_length=16, blank=True, null=True)
    direccion = models.CharField(max_length=128, blank=True, null=True)
    telefono = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        ordering = ('apellido',)
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def get_nombre_completo(self):
        return "{}, {}".format(self.apellido, self.nombre)
