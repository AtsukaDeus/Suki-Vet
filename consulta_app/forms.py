from django.forms import ModelForm
from django import forms
from .models import Consulta

class ConsultaForm(ModelForm):
    fecha_consulta = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    motivo_consulta = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ingrese el motivo de consulta del paciente'}))
    
    # Evaluación general: # comportamiento, postura, movilidad, pelaje, piel
    evaluacion_general = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'En este apartado indique comportamiento, postura, movilidad, pelaje y piel del paciente como evaluacion general'}))
    nutricion = forms.ChoiceField(choices=(('','Selecciona una opción'),('Obeso','Obeso'),('Sobre peso','Sobre peso'),('Peso normal','Peso normal'),('Bajo peso','Bajo peso'),('Muy bajo peso','Muy bajo peso')), widget=forms.Select(attrs={'class':'form-select'}))
    
    # Parametros fisiológicos
    fc = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Frecuencia cardiaca'}))
    fr = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Frecuencia respiratoria'}))
    pc = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Pliegue cutanio'}))
    tllc = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Tiempo de llene capilar'}))
    color_mucosa = forms.ChoiceField(choices=(('Rosa Pálido','Rosa Pálido'),('Rosado Normal','Rosado Normal'),('Rojo Intenso','Rojo Intenso'),('Pálido','Pálido')), widget=forms.RadioSelect(attrs={'class':''}))
    humedad_mucosa = forms.ChoiceField(choices=(('Húmeda normal','Húmeda normal'),('Ligeramente seca','Ligeramente seca'),('Muy seca','Muy seca')), widget=forms.RadioSelect(attrs={'class':''}))
    ev_gang_linf = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Aqui puedes hacer referencia a la evaluación de los ganglios linfáticos'}))
    
    # Conclusión
    comentarios = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Puede ingresar comentarios adicionales referentes a la consulta'}))
    diagnostico = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Diagnostico del paciente'}))
    receta = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Aqui puedes escribir la receta que le has proporcionado al paciente'}))

    class Meta:
        model = Consulta
        fields = ('fecha_consulta','motivo_consulta','evaluacion_general','nutricion','fc','fr','pc','tllc','color_mucosa','humedad_mucosa','ev_gang_linf','comentarios','diagnostico','receta',)
