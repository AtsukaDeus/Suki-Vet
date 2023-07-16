from django.forms import ModelForm, forms
from django.forms import ChoiceField, CharField, Textarea, Select, EmailInput, ModelChoiceField
from django.forms import RadioSelect, TextInput, NumberInput, IntegerField, DecimalField, EmailField
from .models import Direccion, Tutor, Paciente



class DireccionForm(ModelForm):
    ciudad = CharField(max_length=255, widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Ciudad'}))
    comuna = CharField(max_length=255, widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Comuna'}))
    calle = CharField(max_length=255, widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Calle'}))
    no_calle = IntegerField(widget=NumberInput(attrs={'class': 'form-control', 'placeholder': 'Número de Calle'}))
    nro_dpto_casa = IntegerField(widget=NumberInput(attrs={'class': 'form-control', 'placeholder': 'Número de Dpto o Casa'}))
    
    class Meta:
        model = Direccion
        fields = ('ciudad','comuna','calle','no_calle','nro_dpto_casa',)


class TutorForm(ModelForm):
    rut = CharField(max_length=50, widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'RUT'}))
    nombre_tutor = CharField(max_length=255, widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}))
    telefono = CharField(max_length=255, widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono'}))
    email = EmailField(max_length=255, widget=EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    
    class Meta:
        model = Tutor
        fields = ('rut','nombre_tutor','telefono','email',)

        

class PacienteForm(ModelForm):
    nombre_paciente = CharField(max_length=255, widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}))
    edad = IntegerField(required=False, widget=NumberInput(attrs={'class': 'form-control', 'placeholder': 'Edad'}))
    peso = DecimalField(max_digits=5, decimal_places=2, widget=NumberInput(attrs={'class': 'form-control', 'placeholder': 'Peso Kg'}))
    sexo = ChoiceField(choices=(('Macho', 'Macho'), ('Hembra', 'Hembra')), widget=RadioSelect(attrs={'class': ''}))
    esterilizado = ChoiceField(choices=(('Si', 'Sí'), ('No', 'No')), widget=RadioSelect(attrs={'class': ''}))
    vacunas = CharField(widget=Textarea(attrs={'class': 'form-control', 'placeholder': 'Vacunas anteriores y sus fechas o vacunas pendientes'}))
    especie = ChoiceField(choices=(('','Selecciona una opción'),('Perro', 'Perro'), ('Gato', 'Gato')), widget=Select(attrs={'class': 'form-select'}))
    histo_med = CharField(widget=Textarea(attrs={'class': 'form-control', 'placeholder': 'Ingresa historial médico del paciente, enfermedades crónicas, alegías conocidas, medicación actual en caso de haber'}))
    comentarios = CharField(widget=Textarea(attrs={'class': 'form-control', 'placeholder': 'Aqui puedes realizar comentarios referentes al paciente, características, etc...'}))
    
    class Meta:
        model = Paciente
        fields = ('nombre_paciente','edad','peso','sexo','esterilizado','vacunas','especie','histo_med','comentarios',)