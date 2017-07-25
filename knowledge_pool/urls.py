""" Define as urls do knowledge_pool """

from django.conf.urls import url

from . import views

urlpatterns = [
    # Página inicial
    url(r'^$', views.index, name='index'),

    # Página com todos os assuntos
    url(r'^assuntos$', views.assuntos, name='assuntos'),

    # Página com um assunto e suas entradas
    url(r'^assuntos/(?P<assunto_id>\d+)/$', views.assunto, name='assunto'),

    # Página para um novo assunto
    url(r'^novo_assunto/$', views.novo_assunto, name='novo_assunto'),

    # Página para uma nova entrada sobre um assunto específico
    url(r'^nova_entrada/(?P<assunto_id>\d+)/$',
        views.nova_entrada, name='nova_entrada'),

    # Páginas para editar entradas sobre um assunto
    url(r'^editar_entrada/(?P<entrada_id>\d+)/$',
        views.editar_entrada, name='editar_entrada'),
]
