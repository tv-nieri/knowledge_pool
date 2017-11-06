""" Views para o add users """
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render


def logout_view(request):
    """ função de logout do user """
    logout(request)
    return HttpResponseRedirect(reverse('knowledge_pool:index'))


def register(request):
    """ Registro do usuário """
    if request.method != 'POST':
        # Exibe o formulario de cadastro em branco
        form = UserCreationForm()
    else:
        # Processa o formulário preenchido
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Faz login do user e redireciona para a página inicial
            authenticated_user = authenticate(
                username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('knowledge_pool:index'))
    context = {'form': form}
    return render(request, 'users/register.html', context)
