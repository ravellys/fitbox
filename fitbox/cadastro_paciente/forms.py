# from django import forms

from fitbox.cadastro_paciente.models import CadastroPaciente
from bootstrap_modal_forms.forms import BSModalModelForm


class CadastroPacienteForm(BSModalModelForm):
    class Meta:
        model = CadastroPaciente
        fields = ['nome', 'email', 'nascimento', 'sexo']
