# Generated by Django 4.0.4 on 2022-06-04 22:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_remove_donacion_tipodonacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='donacion',
            name='tipoDonacion',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.tipodonacion'),
            preserve_default=False,
        ),
    ]