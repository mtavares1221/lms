from django.db import models
from .disciplina import *


class Usuario(models.Model):
    login = models.TextField(max_length=20, unique=True)
    senha = models.TextField(max_length=20)
    dtExpiracao = models.DateField(default=date(year=1900, month=1, day=1))

class Aluno(Usuario):
    nome = models.TextField(max_length=255)
    email = models.TextField(max_length=255, unique=True)
    celular = models.TextField(max_length=255, unique=True)
    ra = models.TextField(max_length=7)
    foto = models.TextField(max_lengt=255)
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    
    def matriculas(self):
        from .disciplina import SolicitacaoMatricula
        sm = SolicitacaoMatricula.objects.filter(aluno=self)
        return sm

class Professor(Usuario):
    nome = models.TextField(max_length=255)
    email = models.TextField(max_length=255, unique=True)
    celular = models.TextField(max_length=255, unique=True)
    apelido = models.TextField(max_length=255)
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)

class Coordenador(Usuario):
    nome = models.TextField(max_length=255)
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    email = models.TextField(max_length=255, unique=True)
    celular = models.TextField(max_length=255, unique=True)
