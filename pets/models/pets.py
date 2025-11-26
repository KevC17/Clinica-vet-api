from django.db import models

class Pets(models.Model):
    name = models.CharField(max_length=160)
    especie = models.CharField(max_length=160)
    raza = models.CharField(max_length=160)
    color = models.CharField(max_length=160)
    fecha_nacimiento = models.DateField(max_length=160)
    peso_kg = models.DecimalField(max_length=160, decimal_places=2, max_digits=5)
    nombre_duenio = models.CharField(max_length=160)
    telefono_duenio = models.CharField(max_length=160)
    email_duenio = models.CharField(max_length=160)
    estado = models.CharField(max_length=160)
    
    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name