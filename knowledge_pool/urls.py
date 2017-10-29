""" Define as urls do knowledge_pool """

from django.conf.urls import url

from . import views

urlpatterns = [
    # Página inicial
    url(r'^$', views.index, name='index'),

    # Página inicial
    url(r'^about$', views.about, name='about'),

    # Página com todos os assuntos
    url(r'^assuntos$', views.assuntos, name='assuntos'),

    # Página com um assunto e suas entradas
    url(r'^assuntos/(?P<assunto_id>\d+)/$', views.assunto, name='assunto'),

    # Página para um novo assunto
    url(r'^novo_assunto/$', views.novo_assunto, name='novo_assunto'),

    # Deletar um assunto
    url(r'^remover_assunto/(?P<assunto_id>\d+)/$',
        views.remover_assunto, name='remover_assunto'),

    # Confirma remocao assunto
    url(r'^confirma_remocao_assunto/(?P<assunto_id>\d+)/$',
        views.confirma_remocao_assunto, name='confirma_remocao_assunto'),

    # Editar um assunto
    url(r'^editar_assunto/(?P<assunto_id>\d+)/$',
        views.editar_assunto, name='editar_assunto'),

    # Página para uma nova entrada sobre um assunto específico
    url(r'^nova_entrada/(?P<assunto_id>\d+)/$',
        views.nova_entrada, name='nova_entrada'),

    # Páginas para editar entradas sobre um assunto
    url(r'^editar_entrada/(?P<entrada_id>\d+)/$',
        views.editar_entrada, name='editar_entrada'),

    # Confirma remocao entrada
    url(r'^confirma_remocao_entrada/(?P<entrada_id>\d+)/$',
        views.confirma_remocao_entrada, name='confirma_remocao_entrada'),

    # Deletar uma entrada
    url(r'^remover_entrada/(?P<entrada_id>\d+)/$',
        views.remover_entrada, name='remover_entrada'),

    # Apresenta os gráficos.
    url(r'^graficos$', views.graficos, name='graficos'),

    # Entradas do user
    url(r'^minhas_entradas/(?P<user_id>\d+)/$',
        views.minhas_entradas, name='minhas_entradas'),
]
