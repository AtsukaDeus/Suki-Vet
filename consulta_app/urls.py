from django.urls import path
from .views import nuevaConsulta


urlpatterns = [
    path('nueva_consulta/<int:id>', nuevaConsulta, name='nueva_consulta'),
]
