from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

    
class Senai(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.TextField(max_length=1500)
    logo = models.ImageField(upload_to='logo/')

    def __str__(self):
        return self.titulo
    
from django.db import models

class Inventario(models.Model):
    num_inventario = models.CharField(max_length=10, unique=True)
    denominacao = models.CharField(max_length=255)
    localizacao = models.CharField(max_length=10)
    link_imagem = models.URLField(max_length=500, blank=True, null=True) 
    sala = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return f"{self.num_inventario} - {self.denominacao}"
