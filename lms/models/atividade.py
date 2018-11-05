from django.db import models
from .disciplina import *
from .usuario import *


class Atividade(models.model):
    titulo = models.TextField(max_length=255, unique=True)
    descricao = models.TextField(max_length=255)
    conteudo = models.TextField(max_length=255)
    tipo = models.IntegerField()
    extras = models.TextField(max_length=255)
    professor = models.ForeignKey(Professor, on_delete=models.PROTECT)

class AtividadeVinculada(Atividade):
    rotulo = models.TextField(max_length=255)
    status = models.IntegerField(default='Disponibilizada')
    professor = models.ForeignKey(Professor, on_delete=models.PROTECT)
    atividade = models.ForeignKey(Atividade, on_delete=models.PROTECT)
    disciplina_ofertada = models.ForeignKey(DisciplinaOfertada, on_delete=models.PROTECT)
    dtInicioRespostas = models.DateTimeField(default=timezone.now)
    dtFimRespostas = models.DateTimeField()

class entrega(Atividade):
    aluno = models.ForeignKey(Aluno, on_delete=models.PROTECT)
    atividade_vinculada = models.ForeignKey(AtividadeVinculada, on_delete=models.PROTECT)
    titulo = models.TextField(max_length=255)
    resposta = models.TextField(max_length=255)
    obs = models.TextField(max_length=255)
    nota = models.DecimalField(max_digits=2, decimal_places=2)
    status = models.IntegerField(default='Entregue')
    dtAvaliacao = models.DateTimeField()


class Mensagem (models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.PROTECT)
    professor = models.ForeignKey(Professor, on_delete=models.PROTECT)
    assunto = models.TextField(max_length=255)
    referencia = models.TextField(max_length=255)
    conteudo = models.TextField(max_length=255)
    status = models.IntegerField(default='Enviado')
    resposta = models.TextField(max_length=255)
    dtResposta = models.DateTimeField(default=timezone.now)