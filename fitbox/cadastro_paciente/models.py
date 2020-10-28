from django.db import models


# Create your models here.
from django.urls import reverse


class CadastroPaciente(models.Model):
    SEXO_CHOICES = [
        ["F", "Feminino"],
        ["M", "Masculino"]
    ]

    nome = models.CharField(max_length=100)
    nascimento = models.DateField()
    email = models.EmailField(unique=True)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, null=True)
    # slug = models.SlugField(max_length=32, null=True)

    def get_absolute_url(self):
        return reverse('cadastro:dados_paciente', args=(self.id, ))

    def __str__(self):
        return self.nome
