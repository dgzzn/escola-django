"""p1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # alunos
    path('alunos/', views.AlunoListView.as_view(), name='lista-alunos'),
    path('alunos/<int:pk>/', views.AlunoDetailView.as_view(), name='detalhe-aluno'),
    path('alunos/novo/', views.AlunoCreateView.as_view(), name='novo-aluno'),
    path('alunos/<int:pk>/editar/', views.AlunoUpdateView.as_view(), name='alterar-aluno'),
    path('alunos/<int:pk>/excluir/', views.AlunoDeleteView.as_view(), name='excluir-aluno'),
    # cursos 
    path('cursos/', views.CursoListView.as_view(), name='lista-cursos'),
    path('cursos/<int:pk>/', views.CursoDetailView.as_view(), name='detalhe-curso'),
    path('cursos/novo/', views.CursoCreateView.as_view(), name='novo-curso'),
    path('cursos/<int:pk>/editar/', views.CursoUpdateView.as_view(), name='alterar-curso'),
    path('cursos/<int:pk>/excluir/', views.CursoDeleteView.as_view(), name='excluir-curso'),
    # disciplinas
    path('disciplinas/', views.DisciplinaListView.as_view(), name='lista-disciplinas'),
    path('disciplinas/<int:pk>/', views.DisciplinaDetailView.as_view(), name='detalhe-disciplina'),
    path('disciplinas/nova/', views.DisciplinaCreateView.as_view(), name='nova-disciplina'),
    path('disciplinas/<int:pk>/editar/', views.DisciplinaUpdateView.as_view(), name='alterar-disciplina'),
    path('disciplinas/<int:pk>/excluir/', views.DisciplinaDeleteView.as_view(), name='excluir-disciplina'),
    # professores
    path('professores/', views.ProfessorListView.as_view(), name='lista-professores'),
]