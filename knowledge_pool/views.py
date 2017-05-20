""" Arquivo de views(controller) do app knowledge_pool """
from django.shortcuts import render

def index(request):
    """ Retorna página Inicial """
    return render(request, 'knowledge_pool/index.html')
