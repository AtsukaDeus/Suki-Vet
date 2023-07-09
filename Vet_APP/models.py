from django.db import models


class Direccion(models.Model):
    ciudad = models.CharField(max_length=255)
    comuna = models.CharField(max_length=255)
    calle = models.CharField(max_length=255)
    no_calle = models.IntegerField()
    nro_dpto_casa = models.IntegerField()


class Tutor(models.Model):
    rut = models.CharField(max_length=50, primary_key=True)
    nombre_tutor = models.CharField(max_length=255, null=False)
    telefono = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, null=True)
    id_dir = models.ForeignKey(Direccion, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self) -> str:
        return f'{self.rut}'


class Paciente(models.Model):
    nombre_paciente = models.CharField(max_length=255,null=False)
    edad = models.IntegerField(null=False)
    sexo = models.CharField(max_length=255,null=False) #<- M, H
    especie = models.CharField(max_length=255,null=False)
    peso = models.DecimalField(max_digits=255, decimal_places=2,null=False)
    patologias = models.CharField(max_length=10000,null=True)
    esterilizado = models.CharField(max_length=255, null=False) # Si, No
    comentarios = models.CharField(max_length=10000,null=True)
    rut_tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self) -> str:
        return f'Paciente: {self.nombre_paciente}, Tutor: {self.rut_tutor}'


class Consulta(models.Model):
    fecha_consulta = models.DateTimeField(null=False)
    motivo_consulta = models.CharField(max_length=10000,null=False)
    comentarios = models.CharField(max_length=100000, null=False)
    id_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, null=True, blank=True)
    


