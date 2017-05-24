""" Arquivo de views(controller) do app knowledge_pool """
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Assunto
from .forms import AssuntoForm

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
