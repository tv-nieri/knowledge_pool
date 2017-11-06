""" Arquivo de views(controller) do app knowledge_pool """
import json

from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import AssuntoForm, EntradaForm
from .models import Assunto, Entrada
from .utils import *


def index(request):
    """ Retorna página Inicial """
    try:
        user = User.objects.get(id=request.user.id)
        context = {'user': user}
        return render(request, 'knowledge_pool/index.html', context)
    except ObjectDoesNotExist:
        return render(request, 'knowledge_pool/index.html')


def about(request):
    """ About page """
    try:
        user = User.objects.get(id=request.user.id)
        contexto = {'user': user}
        return render(request, 'knowledge_pool/about.html', contexto)
    except ObjectDoesNotExist:
        return render(request, 'knowledge_pool/about.html')


@login_required
def assuntos(request):
    """ Retorna uma página com todos os assuntos """
    lista_assuntos = Assunto.objects.order_by('data_criacao')
    contexto = {'lista_assuntos': lista_assuntos}
    return render(request, 'knowledge_pool/assuntos.html', contexto)


@login_required
def assunto(request, assunto_id):
    """ Retorna um assunto e todas as suas entradas """
    var_assunto = Assunto.objects.get(id=assunto_id)
    user_logado = User.objects.get(id=request.user.id)

    entradas = var_assunto.entrada_set.order_by('-data_criacao')
    contexto = {'assunto': var_assunto, 'entradas': entradas,
                'user_logado': user_logado}
    return render(request, 'knowledge_pool/assunto.html', contexto)


@login_required
def novo_assunto(request):
    """ Cria um novo assunto """
    if request.method != 'POST':
        form = AssuntoForm()
    else:
        form = AssuntoForm(request.POST)
        if form.is_valid():
            novo_assunto = form.save(commit=False)
            novo_assunto.dono = request.user
            novo_assunto.save()
            return HttpResponseRedirect(reverse('knowledge_pool:assuntos'))
    contexto = {'form': form}
    return render(request, 'knowledge_pool/novo_assunto.html', contexto)


@login_required
def editar_assunto(request, assunto_id):
    """ Editar um assunto """
    assunto = Assunto.objects.get(id=assunto_id)

    if request.method != 'POST':
        # Entrega um form com os dados atuais
        form = AssuntoForm(instance=assunto)
    else:
        # Dados submetidos, processa e salva alteração
        form = AssuntoForm(instance=assunto, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('knowledge_pool:assunto', args=[assunto.id]))

    contexto = {'assunto': assunto, 'form': form}
    return render(request, 'knowledge_pool/editar_assunto.html', contexto)


@login_required
def confirma_remocao_assunto(request, assunto_id):
    """ Confirma a remocao de um assunto """
    assunto = Assunto.objects.get(id=assunto_id)
    contexto = {'assunto': assunto}
    return render(request, 'knowledge_pool/confirma_remocao_assunto.html', contexto)


@login_required
def remover_assunto(request, assunto_id):
    """ Remove um assunto """
    assunto = Assunto.objects.get(id=assunto_id)
    assunto.delete()
    return HttpResponseRedirect(reverse('knowledge_pool:assuntos'))


@login_required
def nova_entrada(request, assunto_id):
    """ Cria uma nova entrada sobre um assunto em específico """
    assunto = Assunto.objects.get(id=assunto_id)
    user_logado = User.objects.get(id=request.user.id)

    if request.method != 'POST':
        # Nenhum dado submetido, retorna form em branco.
        form = EntradaForm()
    else:
        # Dados de post submetidos, processa o form.
        form = EntradaForm(data=request.POST)
        if form.is_valid():
            nova_entrada = form.save(commit=False)
            assunto.qnt_entradas += 1
            nova_entrada.assunto = assunto
            nova_entrada.dono = user_logado
            assunto.save()
            nova_entrada.save()

            return HttpResponseRedirect(
                reverse('knowledge_pool:assunto', args=[assunto_id]))
    contexto = {'assunto': assunto, 'form': form}
    return render(request, 'knowledge_pool/nova_entrada.html', contexto)


@login_required
def editar_entrada(request, entrada_id):
    """ Edita uma entrada existente """
    entrada = Entrada.objects.get(id=entrada_id)
    assunto = entrada.assunto

    if request.method != 'POST':
        # Requição inicial, entrega um form com os dados da entrada preenchidos
        form = EntradaForm(instance=entrada)
    else:
        # Dados de post submetidos, processa os dados
        form = EntradaForm(instance=entrada, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(
                reverse('knowledge_pool:assunto', args=[assunto.id]))
    contexto = {'entrada': entrada, 'assunto': assunto, 'form': form}
    return render(request, 'knowledge_pool/editar_entrada.html', contexto)


@login_required
def confirma_remocao_entrada(request, entrada_id):
    """ Confirma a remocao de uma entrada """
    entrada = Entrada.objects.get(id=entrada_id)
    contexto = {'entrada': entrada}
    return render(request, 'knowledge_pool/confirma_remocao_entrada.html', contexto)


@login_required
def remover_entrada(request, entrada_id):
    """ Remove uma entrada """
    entrada = Entrada.objects.get(id=entrada_id)
    assunto = Assunto.objects.get(id=entrada.assunto_id)
    entrada.delete()
    if entrada is not None:
        return HttpResponseRedirect(
            reverse('knowledge_pool:assunto', args=[entrada.assunto.id]))
    else:
        contexto = {"assunto": assunto.id}
        return render(request, 'knoledge_pool/assunto.html', contexto)

@login_required
def graficos(request):
    """ Apresenta os gráficos """
    qtd_entradas = get_qnt_entrada()
    titulos_assuntos = get_titulos_assuntos()
    user_names = get_user_names()
    entradas_por_user = get_entradas_por_user()
    entradas_utilizadas = get_entradas_utilizadas_chart()

    contexto = {"titulos": json.dumps(titulos_assuntos),
                "entradas": json.dumps(qtd_entradas),
                "users": json.dumps(user_names),
                "entradas_por_user": json.dumps(entradas_por_user),
                "assuntos_entradas": json.dumps(entradas_utilizadas['assuntos']),
                "qnt_entradas_utilizadas": json.dumps(entradas_utilizadas['qnt']),
                "entradas_utilizadas": get_entradas_utilizadas()}

    return render(request, 'knowledge_pool/graficos.html', contexto)


@login_required
def minhas_entradas(request, user_id):
    """ Mostra as entradas do user logado """
    user = User.objects.get(id=user_id)
    entradas = user.entrada_set.all()
    assuntos_all = [obj.assunto for obj in entradas]
    assuntos = []
    for assunto in assuntos_all:
        if assunto not in assuntos:
            assuntos.append(assunto)
    contexto = {"user": user,
                "entradas": entradas,
                "assuntos": assuntos}
    return render(request, 'knowledge_pool/minhas_entradas.html', contexto)


@login_required
def soma_utilizacao(request, entrada_id):
    """ Soma 1 na utilização de uma entrada """
    entrada = Entrada.objects.get(id=entrada_id)
    assunto = entrada.assunto
    entrada.qtd_utilizacoes += 1
    entrada.save()
    return HttpResponseRedirect(
        reverse('knowledge_pool:assunto', args=[assunto.id]))


@login_required
def entradas_utilizadas(request):
    """ Mostra as entradas mais utilizadas """
    entradas = get_entradas_utilizadas()
    contexto = {"entradas": entradas}
    return render(request, 'knowledge_pool/entradas_utilizadas.html', contexto)
