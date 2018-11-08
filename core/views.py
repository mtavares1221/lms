from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'title': 'Onlearning - LMS'
    }
    return render(request, "index.html", context)

def adm(request):
    context = {
        'title': 'Onlearning - Curso de Administração'
    }
    return render(request, "pages/cursos/adm/adm.html", context)


def ads(request):
    context = {
        'title': 'Onlearning - Curso de Análise e Desenvolvimento de Sistemas'
    }
    return render(request, "pages/cursos/ads/ads.html", context)


def data_science(request):
    context = {
        'title': 'Onlearning - Curso de Ciência de Dados'
    }
    return render(request, "pages/cursos/dsc/data-science.html", context)

def data_security(request):
    context = {
        'title': 'Onlearning - Curso de Segurança de Dados'
    }
    return render(request, "pages/cursos/dse/data-security.html", context)

def jogos_digitais(request):
    context = {
        'title': 'Onlearning - Curso de Jogos Digitais'
    }
    return render(request, "pages/cursos/jd/jogos-digitais.html", context)

def prod_multimidia(request):
    context = {
        'title': 'Onlearning - Curso de Produção Multimídia'
    }
    return render(request, "pages/cursos/pm/prod-multimidia.html", context)

def noticias(request):
    context = {
        'title': 'Onlearning | Noticias'
    }
    return render(request, "pages/noticias/noticias.html", context)


# Inscrições
def inscricao(request):
    context = {
        'title': 'Onlearning - Inscrever-se'
    }
    return render(request, 'pages/inscricao/inscricao.html', context)

# Login
def login(request):
    context = {
        'title': 'Onlearning - Login'
    }
    return render(request, 'login.html', context)

#Áreas
def area_aluno(request):
    context = {
        'title': 'Onlearning - Área do Aluno'
    }
    return render(request, 'pages/acesso/area-aluno/aluno.html', context)

def area_coordenador(request):
    context = {
        'title': 'Onlearning - Área do Coordenador'
    }
    return render(request, 'pages/acesso/area-coordenador/coordenador.html', context)


def area_professor(request):
    context = {
        'title': 'Onlearning - Área do Professor'
    }
    return render(request, 'pages/acesso/area-professor/professor.html', context)
