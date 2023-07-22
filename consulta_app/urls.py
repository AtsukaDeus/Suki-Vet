from django.urls import path
from .views import nuevaConsulta, historialConsulta, verConsulta


urlpatterns = [
    path('nueva_consulta/<int:id>', nuevaConsulta, name='nueva_consulta'),
    path('historial_consulta/<int:id>', historialConsulta, name='historial_consulta'),
    path('historial_consulta/ver_consulta/<int:id>', verConsulta, name='ver_consulta'),
]
