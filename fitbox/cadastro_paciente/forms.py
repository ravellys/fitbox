from django import forms

from fitbox.cadastro_paciente.models import CadastroPaciente


class CadastroPacienteForm(forms.ModelForm):
    class Meta:
        model = CadastroPaciente
        fields = ('nome', 'email', 'nascimento', 'sexo')
