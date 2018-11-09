# Generated by Django 2.1.2 on 2018-11-06 04:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contabilidad', '0007_auto_20181105_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaccion',
            name='debe',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='transaccion',
            name='descripcion',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='transaccion',
            name='detalle',
            field=models.ManyToManyField(to='contabilidad.DetalleTransaccion'),
        ),
        migrations.AlterField(
            model_name='transaccion',
            name='haber',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='transaccion',
            name='periodo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contabilidad.Periodo'),
        ),
    ]
