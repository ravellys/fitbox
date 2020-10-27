from django.shortcuts import render, redirect
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
