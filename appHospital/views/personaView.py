from rest_framework.response import Response
from rest_framework.decorators import api_view
from appHospital.models.persona import Persona
from appHospital.serializers.serializadorPersona import SerializadorPersona

# @api_view(['GET','POST'])
# def persona_view(request):
#     if request.method =='GET':
#         persona = Persona.objects.all()
#         persona_serializer = SerializadorPersona(persona,many=True)
#         return Response (persona_serializer.data)
    
#     elif request.method =='POST':
#         per_serializer = SerializadorPersona(data=request.data)
#         if  per_serializer.is_valid():
#             per_serializer.save()
#             return Response(per_serializer.data)
#         return Response(per_serializer.errors)
@api_view(['GET','PUT','DELETE'])
def persona_unique_view(request,pk=None):
    persona = Persona.objects.filter(id=pk).first()
    if request.method == 'GET':
        persona_serializer = SerializadorPersona(persona)
        return Response(persona_serializer.data)

    elif request.method == 'PUT':
        request.data
        persona_serializers = SerializadorPersona(persona,data=request.data)
        if  persona_serializers.is_valid():
            persona_serializers.save()
            return Response(persona_serializers.data)
        return Response(persona_serializers.errors)
    
    elif request.method == 'DELETE':
        persona.delete()
        return Response('Eliminado')