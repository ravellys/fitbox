# from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from fitbox.consultas.forms import ConsultaForm
from fitbox.consultas.models import Consulta


class ConsultaCreateView(CreateView):
    template_name = "consultas/cadastro_consulta.html"
    model = Consulta
    form_class = ConsultaForm
    success_url = reverse_lazy("consulta:cadastro_consulta")
