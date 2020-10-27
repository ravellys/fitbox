from django.urls import path

from fitbox.cadastro_paciente.views import cadastro_paciente, indice

app_name = 'cadastro'
urlpatterns = [
    path('', cadastro_paciente, name='cadastro_paciente'),
]
