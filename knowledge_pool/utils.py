""" Utils methods """
from .models import Assunto, Entrada
from django.contrib.auth.models import User
from datetime import datetime

def get_assuntos_qnt_entrada():
    """ Retorna os assuntos com pelo menos 1 entrada """
    assuntos = Assunto.objects.filter(qnt_entradas__gt=0)
    return assuntos


def get_titulos_assuntos():
    """ Retorna o título dos 10 primeiros assuntos com mais entradas """
    assuntos = get_assuntos_qnt_entrada().order_by('-qnt_entradas')[:10]
    titulos_assuntos = [obj.titulo for obj in assuntos]
    return titulos_assuntos


def get_qnt_entrada():
    """ Retorna a quantidade de entradas dos 10 primeiros assuntos com mais entradas """
    assuntos = get_assuntos_qnt_entrada()[:10]
    qtd_entradas = []
    for assunto in assuntos:
        qtd_entradas.append(assunto.entrada_set.count())
    return qtd_entradas


def get_user_names():
    """ Retorna todos os usernames em string """
    users = User.objects.all()
    user_names = []
    for user in users:
        if user.username == "admin":
            continue
        user_names.append(user.username)
    return user_names


def get_entradas_por_user():
    """ Conta as entradas dos users """
    users = User.objects.all()
    entradas_por_user = []
    for user in users:
        if user.username == "admin":
            continue
        entradas_por_user.append(user.entrada_set.count())
    return entradas_por_user
