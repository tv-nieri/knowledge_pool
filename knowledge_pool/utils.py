""" Utils methods """
from .models import Assunto, Entrada
from django.contrib.auth.models import User
from datetime import datetime

def get_assuntos_qnt_entrada():
    assuntos = Assunto.objects.filter(qnt_entradas__gt=0)
    return assuntos


def get_titulos_assuntos():
    assuntos = get_assuntos_qnt_entrada().order_by('-qnt_entradas')[:10]
    titulos_assuntos = [obj.titulo for obj in assuntos]
    return titulos_assuntos


def get_qnt_entrada():
    assuntos = get_assuntos_qnt_entrada()[:10]
    qtd_entradas = []
    for assunto in assuntos:
        qtd_entradas.append(assunto.entrada_set.count())
    return qtd_entradas



