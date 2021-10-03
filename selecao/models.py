from django.db import models
from .functions import validate_CPF

# Create your models here.

# Tabela para Candidato
class Candidato(models.Model):

    DEFICIENCIA = (
        ('S', 'Sim'),
        ('N', 'Não'),
    )

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']

    nome = models.CharField(max_length=60)
    dt_nascimento = models.DateField('Data Nascimento')
    cpf = models.CharField(unique=True, max_length=11, validators=[validate_CPF])
    tel = models.CharField(max_length=11)
    email = models.CharField(max_length=120)
    deficiencia = models.CharField(max_length=1, choices=DEFICIENCIA)
    qual_deficiencia = models.CharField(max_length=200)
    necessidade = models.CharField(max_length=200)
    dt_inclusao = models.DateTimeField(auto_now_add=True)
