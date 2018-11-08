from django.contrib import admin
from django.urls import path
from core.views import *

urlpatterns = [ 
    path('', index),
    path('index', index),
    path('login', login),
    path('inscricao', inscricao),
    path('cursos/adm/', adm),
    path('cursos/ads/', ads),
    path('cursos/dsc/', data_science),
    path('cursos/dse/', data_security),
    path('cursos/jd/', jogos_digitais),
    path('cursos/pm/', prod_multimidia),
    path('area-aluno', area_aluno),
    path('area-coordenador', area_coordenador),
    path('area-professor', area_professor),
    path('noticias/', noticias),
    path('admin/', admin.site.urls),
    
]

