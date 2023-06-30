from django.db import models


class Direccion(models.Model):
    ciudad = models.CharField(max_length=255)
    comuna = models.CharField(max_length=255)
    calle = models.CharField(max_length=255)
    no_calle = models.IntegerField()
    no_dpto_Casa = models.IntegerField()
    

class Tutor(models.Model):
    rut = models.CharField(max_length=50, primary_key=True)
    nombre = models.CharField(max_length=255, null=False, blank=False)
    telefono = models.CharField(max_length=255, null=False, blank=False)
    email = models.CharField(max_length=255)
    id_dir = models.ForeignKey(Direccion, on_delete=models.SET_NULL, null=True)
    

class Paciente(models.Model):
    nombre = models.CharField(max_length=255,null=False, blank=False)    
    sexo = models.CharField(max_length=1,null=False, blank=False) #<- M, H
    especie = models.CharField(max_length=255)
    raza = models.CharField(max_length=255)
    color_pelaje = models.CharField(max_length=255)
    manchas = models.CharField(max_length=2) # Si, No
    color_manchas = models.CharField(max_length=255)
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    patologias = models.CharField(max_length=10000)
    esterilizado = models.CharField(max_length=2, null=False, blank=False) # Si, No
    comentarios = models.CharField(max_length=10000)
    rut_tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE, null=False, blank=False)
    
    
class Consulta(models.Model):
    fecha_consulta = models.DateTimeField()
    comentarios = models.CharField(max_length=100000)
    id_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, null=False)
    
