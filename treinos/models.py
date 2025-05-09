from django.db import models


class Treino(models.Model):
    nome_completo = models.CharField(max_length=100)
    sexo = models.CharField(max_length=10, choices=[(
        'masculino', 'Masculino'), ('feminino', 'Feminino')])
    idade = models.IntegerField()
    identidade = models.CharField(max_length=20)
    setor = models.CharField(max_length=50)
    flexoes = models.IntegerField()
    abdominais = models.IntegerField()
    corrida = models.IntegerField()
    nivel_flexoes = models.CharField(max_length=10)
    nivel_abdominais = models.CharField(max_length=10)
    nivel_corrida = models.CharField(max_length=10)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome_completo} - {self.data_criacao}"
