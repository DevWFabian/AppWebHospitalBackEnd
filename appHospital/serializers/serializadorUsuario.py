from os import set_inheritable
from rest_framework import serializers
from appHospital.models.usuario import Usuario
from appHospital.models.persona import Persona
from appHospital.serializers.serializadorPersona import SerializadorPersona
from drf_writable_nested import WritableNestedModelSerializer

class SerializadorUsuario(serializers.ModelSerializer):
    account = SerializadorPersona()
    class Meta:
        model = Usuario
        fields = ['id','username','password','Estado','account']

    def create(self, validated_data):
        accountData = validated_data.pop('account')
        userInstance = Usuario.objects.create(**validated_data)
        Persona.objects.create(user=userInstance, **accountData)
        print(userInstance)
        return userInstance 
    def update(self,instance,validatad_data):
        instance.username = validatad_data.get('username',instance.username)
        instance.password = validatad_data.get('password',instance.password)
        instance.Estado= validatad_data.get('Estado',instance.Estado)
        instance.save()
        return instance
     
    def to_representation(self, obj):
        user = Usuario.objects.get(id=obj.id)
        account = Persona.objects.get(user = obj.id)
        return {
            "id": user.id,
            "username" : user.username,
            "Estado": user.Estado,
            "account" :{
                "id": account.id,
                "Nombre": account.Nombre,
                "Apellido": account.Apellido,
                "Telefono": account.Telefono,
                "Genero": account.Genero,
                "TipoDocumento": account.TipoDocumento,
                "NumeroDocumento": account.NumeroDocumento,
                "Direccion": account.Direccion,
                "Ciudad": account.Ciudad,
                "FechaNacimiento": account.FechaNacimiento,
                "Correo": account.Correo,
                "Rol": account.Rol
            }
        }
        