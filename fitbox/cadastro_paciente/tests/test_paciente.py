import pytest
from django.urls import reverse
from model_mommy import mommy
from fitbox.cadastro_paciente.models import CadastroPaciente
from fitbox.django_assertions import assert_contains


@pytest.fixture
def paciente(db):
    return mommy.make(CadastroPaciente)


@pytest.fixture
def resp(client, paciente):
    resp = client.get(reverse('cadastro:dados_paciente', args=(paciente.slug, )))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200


def test_nome_paciente(resp, paciente):
    assert_contains(resp, paciente.nome)


def test_email_paciente(resp, paciente):
    assert_contains(resp, paciente.email)


@pytest.fixture
def resp_paciente_not_found(client, paciente):
    return client.get(reverse('cadastro:dados_paciente', args=(paciente.slug+'_video_notfound', )))


def test_status_code_paciente_not_found(resp_paciente_not_found):
    return resp_paciente_not_found.status_code == 404
