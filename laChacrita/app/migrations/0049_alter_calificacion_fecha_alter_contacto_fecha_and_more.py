# Generated by Django 4.0.4 on 2022-06-25 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0048_alter_compra_fecha_alter_pedido_fecha_cierre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calificacion',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='suscripcion',
            name='fecha',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
