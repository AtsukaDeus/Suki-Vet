from django.contrib import admin
from gestion_pacientes.models import Direccion, Tutor, Paciente
from consulta_app.models import Consulta

# Register your models here.
admin.site.register(Direccion)
admin.site.register(Tutor)
admin.site.register(Paciente)
admin.site.register(Consulta)
