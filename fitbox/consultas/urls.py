from django.urls import path

from fitbox.consultas.views import ConsultaCreateView

app_name = 'consulta'
urlpatterns = [
    path('', ConsultaCreateView.as_view(), name='cadastro_consulta'),
    # path('<slug:slug>/', detalhe_paciente, name='consulta'),
]
