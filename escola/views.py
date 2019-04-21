from django.shortcuts import render
#from django.views import generic
from .models import *
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

def index(request):
    return render(request, 'escola/base.html', {})


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


class CursoListView(ListView):
    model = Curso
    


class DisciplinaListView(ListView):
    model = Disciplina
    ordering = ['curso']


class ProfessorListView(ListView):
    model = Professor