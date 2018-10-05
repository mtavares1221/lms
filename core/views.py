from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'title': 'Onlearning - LMS'
    }
    return render(request, "index.html", context)

def lista_cursos(request):
    context = {
        'title': 'Onlearning | Lista de Cursos'
    }
    return render(request, "pages/lista-cursos.html", context)

def detalhe_curso(request):
    context = {
        'title': 'Onlearning | Detalhes do Curso'
    }
    return render(request, "pages/detalhe-curso.html", context)

def disciplina(request):
    context = {
        'title': 'Onlearning | Disciplinas'
    }
    return render(request, "pages/disciplina.html", context)

def noticias(request):
    context = {
        'title': 'Onlearning | Noticias'
    }
    return render(request, "pages/noticias.html", context)