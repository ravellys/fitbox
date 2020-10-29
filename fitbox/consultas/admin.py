# Register your models here.
from django.contrib.admin import register, ModelAdmin

from fitbox.consultas.models import Consulta


@register(Consulta)
class ConsultaAdmin(ModelAdmin):
    list_filter = ('paciente',)
    prepopulated_fields = {'slug': ('descricao', )}
