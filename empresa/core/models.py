from django.db import models
from django.contrib.auth.models import User

class Residencia(models.Model):
    numero = models.IntegerField()
    dueño = models.CharField(max_length=50)
    mail = models.CharField(max_length=50)
    telefono = models.IntegerField()


class Correspondencia(models.Model):
    fecha_recepcion = models.DateField()
    fecha_entrega = models.DateField()
    estado = models.CharField(choices=(
            ('R', "Recibido"),
            ('E', "Entregado"),
        ),
        max_length=1
    )
    destinatario = models.CharField(max_length=50)
    remitente = models.CharField(max_length=50)
    residencia = models.ForeignKey("Residencia", on_delete=models.CASCADE)
    # conserje = models.ForeignKey(User,on_delete=models.SET_NULL,null=True, blank=True)
    

