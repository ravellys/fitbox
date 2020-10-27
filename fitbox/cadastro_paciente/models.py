from django.db import models


# Create your models here.
class CadastroPaciente(models.Model):
    nome = models.CharField(max_length=100)
    nascimento = models.DateField()
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome
