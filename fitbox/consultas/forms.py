# from django import forms
from django.forms import ModelForm
from fitbox.consultas.models import Consulta


class ConsultaForm(ModelForm):
    class Meta:
        model = Consulta
        fields = '__all__'
