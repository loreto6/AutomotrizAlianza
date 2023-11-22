# Generated by Django 4.2.4 on 2023-11-01 22:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='imagenesAutos/')),
                ('modelo', models.CharField(max_length=100)),
                ('valor_inicial', models.FloatField()),
                ('patente', models.CharField(blank=True, max_length=100)),
                ('extras', models.TextField(blank=True)),
                ('fecha', models.DateTimeField(verbose_name='Fecha')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
                ('rut', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio_venta', models.FloatField()),
                ('disponiblidad', models.CharField(max_length=50)),
                ('id_auto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VistaCliente.auto')),
            ],
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(verbose_name='Fecha')),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VistaCliente.cliente')),
                ('id_publicación', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VistaCliente.publicacion')),
            ],
        ),
        migrations.CreateModel(
            name='Informe_Compra_Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_auto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VistaCliente.auto')),
                ('id_venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VistaCliente.venta')),
            ],
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('correo', models.EmailField(max_length=254)),
                ('descripcion', models.TextField()),
                ('id_publicación', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VistaCliente.publicacion')),
            ],
        ),
        migrations.AddField(
            model_name='auto',
            name='marca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VistaCliente.marca'),
        ),
        migrations.AddField(
            model_name='auto',
            name='year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VistaCliente.year'),
        ),
    ]