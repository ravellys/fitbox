from django.urls import path

from fitbox.cadastro_paciente.views import cadastro_paciente, indice, detalhe_paciente, PacientCreateView

app_name = 'cadastro'
urlpatterns = [
    path('', cadastro_paciente, name='cadastro_paciente'),
    path('popup/', PacientCreateView.as_view(), name='cadastro_paciente_popup'),
    path('pacientes/', indice, name='indice'),
    path('pacientes/<slug:slug>/', detalhe_paciente, name='dados_paciente'),
]
