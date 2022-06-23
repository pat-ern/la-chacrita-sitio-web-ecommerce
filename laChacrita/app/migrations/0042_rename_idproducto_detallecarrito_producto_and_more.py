# Generated by Django 4.0.4 on 2022-06-23 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0041_detallecarrito'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detallecarrito',
            old_name='idProducto',
            new_name='producto',
        ),
        migrations.AlterField(
            model_name='detallecarrito',
            name='cantidad',
            field=models.IntegerField(choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']]),
        ),
    ]
