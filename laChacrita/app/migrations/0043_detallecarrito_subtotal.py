# Generated by Django 4.0.4 on 2022-06-23 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0042_rename_idproducto_detallecarrito_producto_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='detallecarrito',
            name='subtotal',
            field=models.IntegerField(default=0),
        ),
    ]
