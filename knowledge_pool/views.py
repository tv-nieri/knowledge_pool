""" Arquivo de views(controller) do app knowledge_pool """
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from .models import Assunto, Entrada
from .forms import AssuntoForm, EntradaForm


def index(request):
    """ Retorna página Inicial """
    try:
        user = User.objects.get(id=request.user.id)
        context = {'user': user}
        return render(request, 'knowledge_pool/index.html', context)
    except ObjectDoesNotExist:
        return render(request, 'knowledge_pool/index.html')


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
            nova_entrada.assunto = assunto
            nova_entrada.dono = user_logado
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
    assunto = Assunto.objects.get(id=entrada.assunto.id)
    contexto = {"assunto": assunto}
    entrada.delete()
    return render(request, 'knowledge_pool/assunto.html', contexto)