# Generated by Django 4.0.4 on 2022-05-13 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_cuotero_tipo_plazo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cuotero',
            options={'ordering': ['monto', 'pagare'], 'verbose_name': 'Cuotero', 'verbose_name_plural': 'Cuotas'},
        ),
        migrations.AddField(
            model_name='cliente',
            name='fecha_nacimiento',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cuotero',
            name='cuotas',
            field=models.PositiveIntegerField(verbose_name='Cantidad de cuotas'),
        ),
        migrations.AlterField(
            model_name='cuotero',
            name='monto',
            field=models.PositiveIntegerField(verbose_name='Monto del préstamo'),
        ),
        migrations.AlterField(
            model_name='cuotero',
            name='tipo_plazo',
            field=models.IntegerField(choices=[(7, 'Semanal'), (8, 'Semanal'), (14, 'Quincenal'), (15, 'Quincenal'), (30, 'Mensual')], verbose_name='Tipo de plazo'),
        ),
    ]
