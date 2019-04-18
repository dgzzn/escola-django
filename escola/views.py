from django.shortcuts import render
from django.views import generic
from .models import *

# Create your views here.

def index(request):
    return render(request, 'escola/base.html', {})


class AlunoListView(generic.ListView):
    model = Aluno






class CursoListView(generic.ListView):
    model = Curso
    


class DisciplinaListView(generic.ListView):
    model = Disciplina
    ordering = ['curso']


class ProfessorListView(generic.ListView):
    model = Professor