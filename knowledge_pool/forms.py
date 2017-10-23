""" Arquivo de formulário para knowledge_pool """

from django import forms

from .models import Assunto, Entrada


class AssuntoForm(forms.ModelForm):
    """ Classe que define um form para o modelo Assunto """
    class Meta:
        """ Classe de dados do Modelo assunto (transforma em campos) """
        model = Assunto
        fields = ['titulo', 'descricao']
        labels = {'titulo': 'Título', 'descricao': 'Descrição'}


class EntradaForm(forms.ModelForm):
    """ Classe que define um form baseado no modelo Entrada """
    class Meta:
        """ define os campos do form baseada nos atributos do modelo """
        model = Entrada
        fields = ['ticket_associado', 'texto']
        labels = {'texto': 'Texto', 'ticket_associado': 'Ticket/Erro'}
        widgets = {'texto': forms.Textarea(attrs={'cols': 80})}
