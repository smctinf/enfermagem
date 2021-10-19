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
    celular = models.CharField(max_length=11)
    tel = models.CharField(max_length=10, blank=True, null=True)
    email = models.CharField(max_length=120)
    deficiencia = models.CharField(max_length=1, choices=DEFICIENCIA)
    qual_deficiencia = models.CharField(max_length=600)
    necessidade = models.CharField(max_length=600)
    ip = models.GenericIPAddressField(protocol='IPv4')
    chave = models.CharField(unique=True, max_length=36)
    dt_inclusao = models.DateTimeField(auto_now_add=True)


# Tabela para Local de Prova
class Local(models.Model):

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']
        verbose_name_plural = "Locais"

    nome = models.CharField(max_length=60)
    rua = models.CharField(max_length=60)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=20)
    cidade = models.CharField(max_length=20)
    dt_inclusao = models.DateTimeField(auto_now_add=True)


# Tabela para Horario
class Horario(models.Model):

    def __str__(self):
        return '%s - %s' % (self.local, self.horario)

    class Meta:
        ordering = ['local', 'horario']
        verbose_name_plural = "Horários"
        verbose_name = "Horário"

    local = models.ForeignKey(Local, on_delete=models.PROTECT)
    horario = models.TimeField()
    dt_inclusao = models.DateTimeField(auto_now_add=True)


# Tabela para Sala
class Sala(models.Model):

    def __str__(self):
        return '%s - %s' % (self.horario, self.sala)

    class Meta:
        ordering = ['horario', 'sala']

    horario = models.ForeignKey(Horario, on_delete=models.PROTECT)
    sala = models.CharField(max_length=5)
    dt_inclusao = models.DateTimeField(auto_now_add=True)


# Tabela para Sala
class Alocacao(models.Model):

    def __str__(self):
        return '%s - %s' % (self.sala, self.candidato)

    class Meta:
        ordering = ['sala', 'candidato']
        verbose_name_plural = "Alocações"
        verbose_name = "Alocação"

    sala = models.ForeignKey(Sala, on_delete=models.PROTECT)
    candidato = models.ForeignKey(Candidato, on_delete=models.PROTECT)
    dt_inclusao = models.DateTimeField(auto_now_add=True)


# Tabela para registrar acessos ao comprovante
class Acesso(models.Model):

    def __str__(self):
        return '%s - %s' % (self.candidato, self.ip)

    class Meta:
        ordering = ['dt_inclusao']

    candidato = models.ForeignKey(Candidato, on_delete=models.PROTECT)
    ip = models.GenericIPAddressField(protocol='IPv4')
    dt_inclusao = models.DateTimeField(auto_now_add=True)
