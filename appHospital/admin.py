from django.contrib import admin
from .models.usuario import Usuario
from .models.persona import Persona


admin.site.register(Usuario)
admin.site.register(Persona)
