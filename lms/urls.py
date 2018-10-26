from django.contrib import admin
from django.urls import path
from core.views import *

urlpatterns = [ 
    path('', index),
    path('index', index),
    path('login', login),
    path('pages/inscricao/inscricao', inscricao),
    path('pages/cursos/adm/', adm),
    path('pages/cursos/ads/', ads),
    path('pages/cursos/dsc/', data_science),
    path('pages/cursos/dse/', data_security),
    path('pages/cursos/jd/', jogos_digitais),
    path('pages/cursos/pm/', prod_multimidia),
    path('pages/noticias/', noticias),
    path('admin/', admin.site.urls),
    
]

