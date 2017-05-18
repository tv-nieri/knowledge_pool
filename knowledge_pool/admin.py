""" Arquivo de admin para knowledge_pool """
from django.contrib import admin
from knowledge_pool.models import Assunto, Entrada

admin.site.register(Assunto)
admin.site.register(Entrada)
