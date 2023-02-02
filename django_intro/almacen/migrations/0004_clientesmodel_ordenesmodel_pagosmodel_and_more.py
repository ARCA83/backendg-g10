# Generated by Django 4.1.5 on 2023-02-02 03:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('almacen', '0003_remove_categoriasmodel_producto_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientesModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
                ('apellido', models.CharField(max_length=45)),
                ('correo', models.CharField(max_length=45)),
                ('dni', models.CharField(max_length=8)),
            ],
            options={
                'db_table': 'clientes',
            },
        ),
        migrations.CreateModel(
            name='OrdenesModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('codigo', models.CharField(max_length=45)),
                ('observacion', models.CharField(max_length=100, null=True)),
                ('estado', models.BooleanField(default=True, null=True)),
                ('cliente_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='almacen.clientesmodel')),
                ('usuario_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'ordenes',
            },
        ),
        migrations.CreateModel(
            name='PagosModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('monto', models.FloatField()),
                ('numero_pago', models.IntegerField()),
                ('orden_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='almacen.ordenesmodel')),
            ],
            options={
                'db_table': 'pagos',
            },
        ),
        migrations.CreateModel(
            name='DetallesOrdenModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField()),
                ('orden_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='almacen.ordenesmodel')),
                ('producto_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='almacen.productosmodel')),
            ],
            options={
                'db_table': 'detalles_orden',
            },
        ),
        migrations.CreateModel(
            name='BoletasPagoModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('codigo', models.CharField(max_length=45)),
                ('total', models.FloatField()),
                ('pago_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='almacen.pagosmodel')),
            ],
            options={
                'db_table': 'boletas_pago',
            },
        ),
    ]
