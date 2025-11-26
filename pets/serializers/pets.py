from rest_framework import serializers
from pets.models import Pets

class PetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pets
        fields = ("id","name", "especie", "raza", "color", "fecha_nacimiento", "peso_kg", "nombre_duenio", "telefono_duenio", "email_duenio", "estado")
