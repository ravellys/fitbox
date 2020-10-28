from fitbox.cadastro_paciente.models import CadastroPaciente


def encontrar_paciente(slug):
    return CadastroPaciente.objects.select_related().get(slug=slug)
