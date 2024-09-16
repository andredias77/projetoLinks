from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models

# Amazon link
class AmazonLink(models.Model):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    amazon_link = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name
# Usuario

class CustomUser(AbstractUser):
    # Campos adicionais
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username

class PaginaProduto(models.Model):
    titulo = models.CharField("Título da Página", max_length=255)
    descricao = models.TextField("Descrição", blank=True, null=True)
    criador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
    
class Link(models.Model):
    nome_produto = models.CharField(max_length=255)
    url = models.URLField()  # URL do produto Amazon
    pagina = models.ForeignKey('PaginaProduto', related_name='links', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_produto

#Usuarios

