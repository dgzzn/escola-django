from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Curso)
admin.site.register(Aluno)
admin.site.register(Professor)
admin.site.register(Disciplina)
admin.site.register(Turma)
admin.site.register(TurmaAluno)