from fitbox.cadastro_paciente.models import CadastroPaciente


def encontrar_paciente(id):
    return CadastroPaciente.objects.select_related().get(id=id)


