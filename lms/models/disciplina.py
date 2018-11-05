from django.db import models
from .usuario import *

class Disciplina(models.Model):
    nome = models.TextField(max_length=255, unique=True)
    pe = models.TextField(max_length=255)
    competencias = models.TextField(max_length=255)
    habilidades = models.TextField(max_length=255)
    ementa = models.TextField(max_length=255)
    cp = models.TextField(max_length=255)
    bb = models.TextField(max_length=255)
    bc = models.TextField(max_length=255)
    coordenador = models.ForeignKey(Coordenador, on_delete=models.PROTECT)
    status = models.IntegerField(default='Aberta')
    ch = models.IntegerField()
    pp = models.IntegerField()
    pt = models.IntegerField()
    data = models.DateTimeField(default=timezone.now)


class Curso(models.Model):
    nome = models.TextField(max_length=255, unique=True)

class DisciplinaOfertada(models.Model):
    metodologia = models.TextField(max_length=255)
    recursos = models.TextField(max_length=255)
    ca = models.TextField(max_length=255)
    pa = models.TextField(max_length=255)
    professor = models.ForeignKey(Professor, on_delete=models.PROTECT)
    coordenador = models.ForeignKey(Coordenador, on_delete=models.PROTECT)
    ano = models.IntegerField()
    semestre = models.IntegerField()
    turma = models.IntegerField
    disciplina = models.ForeignKey(Disciplina, on_delete=models.PROTECT)
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT)
    dtInicio = models.DateTimeField(default=timezone.now)
    dfFim = models.DateTimeField(default=timezone.now)

class SolicitacaoMatricula(models.Model):
    status = models.IntegerField(default='Solicitada')
    aluno = models.ForeignKey(Aluno, on_delete=models.PROTECT)
    Coordenador = models.ForeignKey(Coordenador, on_delete=models.PROTECT)
    disciplina_ofertada = models.ForeignKey(DisciplinaOfertada, on_delete=models.PROTECT)
    dtSolicitacao = models.DateTimeField(default=timezone.now)
    
