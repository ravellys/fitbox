from django.urls import path

from fitbox.cadastro_paciente.views import cadastro_paciente, indice, detalhe_paciente

app_name = 'cadastro'
urlpatterns = [
    path('', cadastro_paciente, name='cadastro_paciente'),
    path('pacientes/', indice, name='indice'),
    path('pacientes/<slug:slug>/', detalhe_paciente, name='dados_paciente'),
]
