from django.db import models
from django.contrib.auth.models import User

class Estado(models.Model):
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=2)

    def __str__(self):
        return self.nome

class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, related_name="cidades")
    dono = models.ForeignKey(User, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='cidades_fotos/', null=True, blank=True)

    def __str__(self):
        return self.nome
