from django.db import models
# Create your models here.
#Para cada Reserva se necesita almacenar, su ID, nombre de la persona que realiza la 
# reserva, teléfono, la fecha de reserva, la hora, la cantidad de personas, el correo 
#electrónico, el estado (RESERVADO, COMPLETADA, ANULADA, NO ASISTEN) y una 
#observación.

class Reserva(models.Model):
    ESTADO_CHOICES = [
        ('RESERVADO', 'Reservado'),
        ('COMPLETADA', 'Completada'),
        ('ANULADA', 'Anulada'),
        ('NO_ASISTEN', 'No Asisten'),
    ]

    nombre=models.CharField(max_length=50)
    telefono=models.CharField(max_length=9)
    fechaReserva=models.DateField()
    hora=models.TimeField()
    cantidadPersonas=models.IntegerField()
    email=models.EmailField()
    estado = models.CharField(max_length=15, choices=ESTADO_CHOICES, default='RESERVADO')
    observacion = models.TextField(blank=True)
