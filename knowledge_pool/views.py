""" Arquivo de views(controller) do app knowledge_pool """
from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from .models import Assunto, Entrada
from .forms import AssuntoForm, EntradaForm


def index(request):
    """ Retorna página Inicial """
    return render(request, 'knowledge_pool/index.html')


@login_required
def assuntos(request):
    """ Retorna uma página com todos os assuntos """
    lista_assuntos = Assunto.objects.filter(dono=request.user).order_by('data_criacao')
    contexto = {'lista_assuntos': lista_assuntos}
    return  render(request, 'knowledge_pool/assuntos.html', contexto)


@login_required
def assunto(request, assunto_id):
    """ Retorna um assunto e todas as suas entradas """
    var_assunto = Assunto.objects.get(id=assunto_id)
    # Garante que o user logado é dono do assunt
    confere_dono(var_assunto, request.user)

    entradas = var_assunto.entrada_set.order_by('-data_criacao')
    contexto = {'assunto': var_assunto, 'entradas': entradas}
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
    context = {'form': form}
    return render(request, 'knowledge_pool/novo_assunto.html', context)


@login_required
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


@login_required
def editar_entrada(request, entrada_id):
    """ Edita uma entrada existente """
    entrada = Entrada.objects.get(id=entrada_id)
    assunto = entrada.assunto
    confere_dono(assunto, request.user)

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

def confere_dono(assunto, user_logado):
    """ Confere se o assunto pertence ao atual user """
    if assunto.dono != user_logado:
        raise  Http404
