# Generated by Django 4.2.7 on 2023-11-28 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=9)),
                ('fechaReserva', models.DateField()),
                ('hora', models.DateTimeField()),
                ('cantidadPersonas', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('estado', models.CharField(choices=[('RESERVADO', 'Reservado'), ('COMPLETADA', 'Completada'), ('ANULADA', 'Anulada'), ('NO_ASISTEN', 'No Asisten')], default='RESERVADO', max_length=15)),
                ('observacion', models.TextField()),
            ],
        ),
    ]
