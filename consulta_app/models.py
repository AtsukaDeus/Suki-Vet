from django.db import models
from gestion_pacientes.models import Paciente



class Consulta(models.Model):
    fecha_consulta = models.DateTimeField(null=False, blank=False)
    motivo_consulta = models.CharField(max_length=10000,null=False)
    
    # Evaluación general:
    # comportamiento, postura, movilidad, pelaje, piel
    evaluacion_general = models.CharField(max_length=100000, null=True, blank=False) 
    nutricion = models.CharField(max_length=255, null=True, blank=False) # obeso, sobre peso, peso normal, bajo peso, muy bajo peso
    
    # Parametros fisiológicos
    fc = models.IntegerField(null=True, blank=False) # frecuencia cardiaca
    fr = models.IntegerField(null=True, blank=False) # frecuencia respiratoria
    pc = models.IntegerField(null=True, blank=False) # pliegue cutanio
    tllc = models.IntegerField(null=True, blank=False) # tiempo de llene capilar
    color_mucosa = models.CharField(max_length=255, null=True, blank=False)
    humedad_mucosa = models.CharField(max_length=255, null=True, blank=False)
    ev_gang_linf = models.CharField(max_length=10000, null=True, blank=False)
    
    # Conclusión
    comentarios = models.CharField(max_length=10000, null=True, blank=True)
    diagnostico = models.CharField(max_length=2000, null=True, blank=False)
    receta = models.CharField(max_length=10000, null=True, blank=False)
    
    id_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, null=True, blank=False)

