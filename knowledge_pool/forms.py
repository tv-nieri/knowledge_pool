""" Arquivo de formulário para knowledge_pool """

from django import forms

from .models import Assunto, Entrada


class AssuntoForm(forms.ModelForm):
    """ Classe que define um form para o modelo Assunto """
    class Meta:
        """ Classe de dados do Modelo assunto (transforma em campos) """
        model = Assunto
        fields = ['titulo', 'descricao', 'ticket_associado']
        labels = {'titulo': 'Título', 'descricao': 'Descrição',
                            'ticket_associado': 'Ticket'}


class EntradaForm(forms.ModelForm):
    """ Classe que define um form baseado no modelo Entrada """
    class Meta:
        """ define os campos do form baseada nos atributos do modelo """
        model = Entrada
        fields = ['texto']
        labels = {'texto': ''}
        widgets = {'texto': forms.Textarea(attrs={'cols': 80})}
