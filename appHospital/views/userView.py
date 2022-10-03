
from django.conf import settings
from rest_framework import generics, status,views
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.permissions import IsAuthenticated
from appHospital.models.usuario import Usuario
from appHospital.serializers.serializadorUsuario import SerializadorUsuario

class UserPostView(views.APIView):
    
    def post(self, request, *args, **kwargs):
        serializer = SerializadorUsuario(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        tokenData = {"username":request.data["username"],
                    "password":request.data["password"]}
        tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)
        return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED)
  
    
class UserGetView(generics.RetrieveAPIView):
    queryset = Usuario.objects.all()
    serializer_class = SerializadorUsuario
    permission_classes = (IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)
        if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Peticion no autorizada'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        return super().get(request, *args, **kwargs)

class UserPutView(views.APIView):
    def put(self, request,pk=None,*args, **kwargs):
            user = Usuario.objects.filter(id = pk).first()                     
            user_serializer = SerializadorUsuario(user,data=request.data)
            if user_serializer.is_valid(raise_exception=True):
                    user_serializer.save()
                    return Response(user_serializer.data,status = status.HTTP_200_OK)            
            return Response(user_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
class UserDeleteView(views.APIView):
    def delete(self, request, pk = None):
        post = Usuario.objects.filter(id = pk).first()
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)