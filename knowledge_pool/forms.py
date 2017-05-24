""" Arquivo de formulário para knowledge_pool """

from django import forms

from .models import Assunto

class AssuntoForm(forms.ModelForm):
    """ Classe que define um form para o modelo Assunto """
    class Meta:
        """ Classe de dados do Modelo assunto (transforma em campos) """
        model = Assunto
        fields = ['titulo']
        labels = {'titulo': ''}
