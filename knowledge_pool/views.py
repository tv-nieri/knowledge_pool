""" Arquivo de views(controller) do app knowledge_pool """
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Assunto, Entrada
from .forms import AssuntoForm, EntradaForm


def index(request):
    """ Retorna página Inicial """
    return render(request, 'knowledge_pool/index.html')


def assuntos(request):
    """ Retorna uma página com todos os assuntos """
    lista_assuntos = Assunto.objects.order_by('data_criacao')
    contexto = {'lista_assuntos': lista_assuntos}
    return  render(request, 'knowledge_pool/assuntos.html', contexto)


def assunto(request, assunto_id):
    """ Retorna um assunto e todas as suas entradas """
    var_assunto = Assunto.objects.get(id=assunto_id)
    entradas = var_assunto.entrada_set.order_by('-data_criacao')
    contexto = {'assunto': var_assunto, 'entradas': entradas}
    return render(request, 'knowledge_pool/assunto.html', contexto)


def novo_assunto(request):
    """ Cria um novo assunto """
    if request.method != 'POST':
        form = AssuntoForm()
    else:
        form = AssuntoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('knowledge_pool:assuntos'))
    context = {'form': form}
    return render(request, 'knowledge_pool/novo_assunto.html', context)


def nova_entrada(request, assunto_id):
    """ Cria uma nova entrada sobre um assunto em específico """
    assunto = Assunto.objects.get(id=assunto_id)

    if request.method != 'POST':
        # Nenhum dado submetido, retorna form em branco.
        form = EntradaForm()
    else:
        # Dados de post submetidos, processa o form.
        form = EntradaForm(data=request.POST)
        if form.is_valid():
            nova_entrada = form.save(commit=False)
            nova_entrada.assunto = assunto
            nova_entrada.save()
            return HttpResponseRedirect(reverse('knowledge_pool:assunto', args=[assunto_id]))
    context = {'assunto': assunto, 'form': form}
    return render(request, 'knowledge_pool/nova_entrada.html', context)


def editar_entrada(request, entrada_id):
    """ Edita uma entrada existente """
    entrada = Entrada.objects.get(id=entrada_id)
    assunto = entrada.assunto

    if request.method != 'POST':
        #Requição inicial, entrega um form com os dados da entrada preenchidos.
        form = EntradaForm(instance=entrada)
    else:
        # Dados de post submetidos, processa os dados
        form = EntradaForm(instance=entrada, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('knowledge_pool:assunto', args=[assunto.id]))
    context = {'entrada': entrada, 'assunto': assunto, 'form': form}
    return render(request, 'knowledge_pool/editar_entrada.html', context)
