from django.contrib import admin
from django.urls import path
from core.views import *

urlpatterns = [ 
    path('', index),
    path('pages/lista-cursos.html', lista_cursos, name='lista_cursos'),
    path('pages/detalhe-curso.html', detalhe_curso, name='detalhe_curso'),
    path('pages/disciplina.html', disciplina, name='disciplina'),
    path('pages/noticias.html', noticias, name='noticias'),
    path('admin/', admin.site.urls),
    
]
