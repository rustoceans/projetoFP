from django.shortcuts import render, HttpResponseRedirect

from pessoas.models import Pessoa

def index(request):
   	return render(request, 'index.html')

def pessoaListar(request):
    #pessoas = Pessoa.objects.all()[0:10]
    pessoas = []
    pessoas.append(Pessoa(nome='UNIFRAN', email='EMAIL', telefone='(35) 3544-1656'))
    pessoas.append(Pessoa(nome='CRUZEIRO'))

    return render(request, 'pessoas/listaPessoas.html', {'pessoas': pessoas})

def pessoaAdicionar(request):
	return render(request, 'pessoas/formPessoas.html)