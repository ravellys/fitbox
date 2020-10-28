from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin, register

from fitbox.cadastro_paciente.models import CadastroPaciente

@register(CadastroPaciente)
class VideoAdmin(ModelAdmin):
    list_display = ('nome', 'email')
    ordering = ('nome', )
    prepopulated_fields = {'slug': ('nome',)}
