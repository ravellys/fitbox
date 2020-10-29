from django.db import models
from django.urls import reverse

from fitbox.cadastro_paciente.models import CadastroPaciente


class Consulta(models.Model):
    paciente = models.ForeignKey(CadastroPaciente, on_delete=models.PROTECT)
    descricao = models.CharField(max_length=32)
    data = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)

    altura = models.PositiveIntegerField()
    peso = models.DecimalField(max_digits=8, decimal_places=2)
    imc = models.DecimalField(max_digits=8, decimal_places=2)
    peso_ideal = models.DecimalField(max_digits=8, decimal_places=2)

    # Circunferências
    # Membros
    # Superiores
    braco_relaxado_direito = models.DecimalField(max_digits=8, decimal_places=2)
    braco_relaxado_esquerdo = models.DecimalField(max_digits=8, decimal_places=2)
    braco_contraido_direito = models.DecimalField(max_digits=8, decimal_places=2)
    braco_contraido_esquerdo = models.DecimalField(max_digits=8, decimal_places=2)

    antebraco_direito = models.DecimalField(max_digits=8, decimal_places=2)
    antebraco_esquerdo = models.DecimalField(max_digits=8, decimal_places=2)
    punho_direito = models.DecimalField(max_digits=8, decimal_places=2)
    punho_esquerdo = models.DecimalField(max_digits=8, decimal_places=2)

    # Inferiores
    panturrilha_direita = models.DecimalField(max_digits=8, decimal_places=2)
    panturrilha_esquerda = models.DecimalField(max_digits=8, decimal_places=2)
    coxa_direita = models.DecimalField(max_digits=8, decimal_places=2)
    coxa_esquerda = models.DecimalField(max_digits=8, decimal_places=2)
    coxa_proximal_direita = models.DecimalField(max_digits=8, decimal_places=2)
    coxa_proximal_esquerda = models.DecimalField(max_digits=8, decimal_places=2)

    # Tronco
    pescoco = models.DecimalField(max_digits=8, decimal_places=2)
    ombro = models.DecimalField(max_digits=8, decimal_places=2)
    cintura = models.DecimalField(max_digits=8, decimal_places=2)
    abdomen = models.DecimalField(max_digits=8, decimal_places=2)
    quadril = models.DecimalField(max_digits=8, decimal_places=2)

    # Composição corporal(pregas cutâneas / bioimpedância) pregas(Durnin & Womersley)
    biceps = models.DecimalField(max_digits=8, decimal_places=2)
    abdominal = models.DecimalField(max_digits=8, decimal_places=2)
    triceps = models.DecimalField(max_digits=8, decimal_places=2)
    suprailiaca = models.DecimalField(max_digits=8, decimal_places=2)
    subescapula = models.DecimalField(max_digits=8, decimal_places=2)

    objetos = models.Manager()

    def __str__(self):
        return self.paciente

    def get_absolute_url(self):
        return reverse('consultas:cadastro_consulta', kwargs={'slug': self.slug})
