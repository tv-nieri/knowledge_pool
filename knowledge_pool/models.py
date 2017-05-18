""" Models da app Knowledge_Pool"""
from django.db import models

class Assunto(models.Model):
    """ Classe que represneta uma assunto """
    titulo = models.CharField(max_length=200)
    data_criacao =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """ Devolve o titulo do assunto """
        return self.titulo


