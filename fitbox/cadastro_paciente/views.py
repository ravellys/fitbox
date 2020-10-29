from bootstrap_modal_forms.generic import BSModalCreateView
from django.shortcuts import render, redirect
# from django.views.generic import ListView
from django.urls import reverse_lazy

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


class PacientCreateView(BSModalCreateView):
    template_name = 'cadastro_paciente/cadastro_paciente_popup.html'
    form_class = CadastroPacienteForm
    success_message = 'Success: pacint was created.'
    success_url = reverse_lazy('base:home')


def indice(request):
    pacientes = CadastroPaciente.objects.order_by('nome').all()
    return render(request, 'cadastro_paciente/paciente.html',
                  context={"pacientes": pacientes})


def detalhe_paciente(request, slug):
    paciente = facade.encontrar_paciente(slug)
    return render(request, 'cadastro_paciente/dados_paciente.html', {'paciente': paciente})
