import pytest
from django.urls import reverse
from model_mommy import mommy
from fitbox.cadastro_paciente.models import CadastroPaciente
from fitbox.django_assertions import assert_contains


@pytest.fixture
def pacientes(db):
    return mommy.make(CadastroPaciente, 3)


@pytest.fixture
def resp(client, pacientes):
    return client.get(reverse('cadastro:indice'))


def test_status_code(resp):
    assert resp.status_code == 200


def test_nome_pacientes(resp, pacientes):
    for paciente in pacientes:
        assert_contains(resp, paciente.nome)
