from django.db import models
from django.urls import reverse

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    duracao = models.IntegerField()

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse("detalhe-curso", kwargs={"pk": self.pk})
    
    

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.IntegerField(verbose_name='Matrícula')
    telefone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse("detalhe-aluno", kwargs={"pk": self.pk})
        

class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
    
    def get_absolute_url(self):
        return reverse("lista-disciplinas")

class Professor(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.IntegerField()
    telefone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.nome

class Turma(models.Model):
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)

class TurmaAluno(models.Model):
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)

