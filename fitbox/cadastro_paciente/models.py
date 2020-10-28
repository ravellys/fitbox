from django.db import models


# Create your models here.
from django.template.defaultfilters import slugify
from django.urls import reverse


class CadastroPaciente(models.Model):
    SEXO_CHOICES = [
        ["F", "Feminino"],
        ["M", "Masculino"]
    ]

    nome = models.CharField(max_length=32)
    nascimento = models.DateField()
    email = models.EmailField(unique=True)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, null=True)
    creation = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=32)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nome)
        super(CadastroPaciente, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('cadastro:dados_paciente', args=(self.slug, ))

    def __str__(self):
        return self.nome
