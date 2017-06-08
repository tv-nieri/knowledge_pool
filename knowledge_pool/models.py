""" Models da app Knowledge_Pool"""
from django.db import models
from django.contrib.auth.models import User

class Assunto(models.Model):
    """ Classe que represneta uma assunto """
    titulo = models.CharField(max_length=200)
    data_criacao = models.DateTimeField(auto_now_add=True)
    dono = models.ForeignKey(User)

    def __str__(self):
        """ Devolve o titulo do assunto """
        return self.titulo

class Entrada(models.Model):
    """ Classe que define uma entrada sobre um assunto """
    assunto = models.ForeignKey(Assunto)
    texto = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """ Retorna uma representação do assunto. """
        if len(self.texto) > 50:
            return self.texto[:50] + "..."
        else:
            return self.texto
