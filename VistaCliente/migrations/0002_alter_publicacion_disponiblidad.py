# Generated by Django 4.2.4 on 2023-11-01 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VistaCliente', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='disponiblidad',
            field=models.CharField(default='Activo', max_length=50),
        ),
    ]