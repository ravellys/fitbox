from django.shortcuts import render, redirect
# from django.views.generic import ListView

from fitbox.cadastro_paciente import facade
from fitbox.cadastro_paciente.forms import CadastroPacienteForm
from fitbox.cadastro_paciente.models import CadastroPaciente


def cadastro_paciente(request):
    form = CadastroPacienteForm()
    if request.method == 'POST':
        form = CadastroPacienteForm(request.POST)
        if form.is_valid():
            print('saving')
            form.save(commit=True)
            return redirect('/cadastro_paciente')
        else:
            print("error")

    return render(request, 'cadastro_paciente/cadastro_paciente.html', context={"form": form})


def indice(request):
    pacientes = CadastroPaciente.objects.order_by('nome')
    return render(request, 'cadastro_paciente/paciente.html',
                  context={"pacientes": pacientes})


def detalhe_paciente(request, id):
    paciente = facade.encontrar_paciente(id)
    return render(request, 'cadastro_paciente/dados_paciente.html', {'paciente': paciente})
