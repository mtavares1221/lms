from django.db import models
from .usuario import *

class Disciplina(models.Model):
    nome = models.TextField(max_length=255, unique=True)
    data = models.DateField()
    status = models.TextField(max_length=255)
    plano_ensino = models.TextField(max_length=5000)
    carga_horaria = models.IntegerField()
    competencias = models.TextField(max_length=1000)
    habilidades = models.TextField(max_length=1000)
    ementa = models.TextField(max_length=5000)
    conteudo_programatico = models.TextField(max_length=5000)
    bibliografia_basica = models.TextField(max_length=1000)
    bibliografia_complementar = models.TextField(max_length=1000)
    percentual_pratico = models.DecimalField(max_digits=13, decimal_places=2)
    percentual_teorico = models.DecimalField(max_digits=13, decimal_places=2)
    coordenador = models.ForeignKey(Coordenador, on_delete=models.PROTECT)



class Curso(models.Model):
    nome = models.TextField(max_length=255, unique=True)

class DisciplinaOfertada(models.Model):
    dt_inicio = models.DateField()
    dt_fim = models.DateField()
    ano = models.IntegerField()
    semestre = models.IntegerField()
    turma = models.TextField(max_length=1)
    metodologia = models.TextField(max_length=255)
    recursos = models.TextField(max_length=255)
    criterio_avaliacao = models.TextField(max_length=1000)
    plano_aula = models.TextField(max_length=1000)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.PROTECT)
    professor = models.ForeignKey(Professor, on_delete=models.PROTECT)
    coordenador = models.ForeignKey(Coordenador, on_delete=models.PROTECT)
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT)

    class Meta:
        unique_together = ('curso', 'disciplina', 'turma', 'ano', 'semestre')

class SolicitacaoMatricula(models.Model):
    dt_solicitacao = models.DateField()
    status = models.TextField(max_length=255)
    aluno = models.ForeignKey(Aluno, on_delete=models.PROTECT)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.PROTECT)
    coordenador = models.ForeignKey(Coordenador, on_delete=models.PROTECT)
