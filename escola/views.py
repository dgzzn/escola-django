from django.shortcuts import render
#from django.views import generic
from .models import *
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

def index(request):
    return render(request, 'escola/base.html', {})

#aluno
class AlunoListView(ListView):
    model = Aluno

class AlunoDetailView(DetailView):
    model = Aluno

class AlunoCreateView(CreateView):
    model = Aluno
    fields = ['nome', 'matricula', 'telefone', 'email']

class AlunoUpdateView(UpdateView):
    model = Aluno
    fields = ['nome', 'matricula', 'telefone', 'email']

class AlunoDeleteView(DeleteView):
    model = Aluno
    success_url = reverse_lazy('lista-alunos')

#curso
class CursoListView(ListView):
    model = Curso

class CursoDetailView(DetailView):
    model = Curso

class CursoCreateView(CreateView):
    model = Curso
    fields = ['nome', 'duracao']

class CursoUpdateView(UpdateView):
    model = Curso
    fields = ['nome', 'duracao']

class CursoDeleteView(DeleteView):
    model = Curso
    success_url = reverse_lazy('lista-cursos')

# disciplina
class DisciplinaListView(ListView):
    model = Disciplina
    ordering = ['curso']

class DisciplinaDetailView(DetailView):
    model = Disciplina

class DisciplinaCreateView(CreateView):
    model = Disciplina
    fields = ['nome', 'curso']

class DisciplinaUpdateView(UpdateView):
    model = Disciplina
    fields = ['nome', 'curso']

class DisciplinaDeleteView(DeleteView):
    model = Disciplina
    success_url = reverse_lazy('lista-disciplinas')
    

class ProfessorListView(ListView):
    model = Professor