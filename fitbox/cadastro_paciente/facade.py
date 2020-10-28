from django.shortcuts import get_object_or_404

from fitbox.cadastro_paciente.models import CadastroPaciente


def encontrar_paciente(slug):
    return get_object_or_404(CadastroPaciente, slug=slug)
