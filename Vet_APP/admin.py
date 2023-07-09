from django.contrib import admin
from .models import Direccion, Tutor, Paciente, Consulta

# Register your models here.
admin.site.register(Direccion)
admin.site.register(Tutor)
admin.site.register(Paciente)
admin.site.register(Consulta)
