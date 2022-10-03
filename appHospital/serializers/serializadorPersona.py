from appHospital.models.persona import Persona
from rest_framework import serializers

class SerializadorPersona(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ['Nombre','Apellido','Telefono','Genero','TipoDocumento','NumeroDocumento','Direccion','Ciudad','FechaNacimiento','Correo','Rol']

