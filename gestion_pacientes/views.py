from django.shortcuts import render, get_object_or_404, redirect
from .models import Paciente, Direccion, Tutor
from .forms import DireccionForm, TutorForm, PacienteForm
from django.contrib import messages

# Create your views here.

def mostrarPacientes(request):
    pacientes = Paciente.objects.order_by('id')
    return render(request, 'index_filtro/mostrar_pacientes.html', {'pacientes': pacientes})


def filtrarPacientes(request):
    rut_tutor = request.POST.get('rut')
    pacientes = Paciente.objects.filter(rut_tutor=rut_tutor)
    encontrado = pacientes.count()
    
    if rut_tutor == '':
        rut_tutor = True
    else:
        rut_tutor = False
    
    return render(request, 'index_filtro/filtrar_pacientes.html', {
        'pacientes': pacientes, 
        'encontrado': encontrado,
        'rut_tutor': rut_tutor,
        })
    
# import pdb;  pdb.set_trace()


def ingresarPaciente(request): 

    if request.method == 'POST':
        direccion_form = DireccionForm(request.POST)
        tutor_form = TutorForm(request.POST)
        paciente_form = PacienteForm(request.POST)
        
        if direccion_form.is_valid() and tutor_form.is_valid() and paciente_form.is_valid():
            direccion = direccion_form.save()
            tutor = tutor_form.save(commit=False)
            tutor.id_dir = direccion
            tutor.save()
            paciente = paciente_form.save(commit=False)
            paciente.rut_tutor = tutor
            paciente.save()
            
            messages.success(request, 'Paciente Ingresado!')
            return redirect('mostrar_pacientes')
    else: 
        direccion_form = DireccionForm()
        tutor_form = TutorForm()
        paciente_form = PacienteForm()
        
    return render(request, 'ingreso_paciente/ingresar_paciente.html', {
        'direccion_form' : direccion_form,
        'tutor_form' : tutor_form,
        'paciente_form' : paciente_form,
    })


def editarPaciente(request, id):
    paciente = Paciente.objects.get(pk=id)
    tutor = Tutor.objects.get(pk=paciente.rut_tutor)
    
    if request.method == 'POST':
        paciente_form = PacienteForm(request.POST, instance=paciente)
        tutor_form = TutorForm(request.POST, instance=tutor)
        direccion_form = DireccionForm(request.POST, instance=tutor.id_dir)
        
        if paciente_form.is_valid() and tutor_form.is_valid() and direccion_form.is_valid():
            direccion = direccion_form.save(commit=False)
            tutor = tutor_form.save(commit=False)
            paciente = paciente_form.save(commit=False)
            
            direccion.save()
            tutor.save()
            paciente.save()
                        
            messages.success(request, 'Datos del paciente actualizados!')
            return redirect('mostrar_pacientes')
    
    else:
        paciente_form = PacienteForm(instance=paciente)
        tutor_form = TutorForm(instance=tutor)
        direccion_form = DireccionForm(instance=tutor.id_dir)

    return render(request, 'ingreso_paciente/editar_paciente.html',{
        'paciente_form' : paciente_form,
        'direccion_form' : direccion_form,
        'tutor_form' : tutor_form,
    })