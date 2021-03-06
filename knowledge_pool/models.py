""" Models da app Knowledge_Pool"""
from django.db import models
from django.contrib.auth.models import User


class Assunto(models.Model):
    """ Classe que representa uma assunto """
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    dono = models.ForeignKey(User)
    qnt_entradas = models.IntegerField(default=0)

    def __str__(self):
        """ Devolve o titulo do assunto """
        return self.titulo


class Entrada(models.Model):
    """ Classe que define uma entrada sobre um assunto """
    assunto = models.ForeignKey(Assunto)
    ticket_associado = models.CharField(max_length=50, blank=True)
    texto = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    dono = models.ForeignKey(User)
    qtd_utilizacoes = models.IntegerField(default=0)

    def __str__(self):
        """ Retorna uma representação do assunto. """
        if len(self.texto) > 50:
            return self.texto[:50] + "..."
        else:
            return self.texto
