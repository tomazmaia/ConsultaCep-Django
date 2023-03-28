import requests
from django.shortcuts import render, redirect
from .coreFiltro import tratamentoBusca
from .coreFiltro.tratamentoBusca import TratamentoBusca


# Create your views here.

def home(request):
    return render(request,'index.html')

def consultar(request):
    cep = request.POST.get("cep")
    tratamento = TratamentoBusca()
    cepQuantidadeENumeralOk= tratamento.tratQuantidadeENumeral(cep)
    if cepQuantidadeENumeralOk is True:
        naoLocalizado = {'Nao': 'localizado'}
        response = requests.get('https://viacep.com.br/ws/{}/json'.format(cep))
        data = response.json()
        if 'erro' in data:
            context = {'data': naoLocalizado}
        else:
            context = {'data': data}
    return render(request,'resultadoBusca.html',context)

def retornar(request):
    voltar = request.POST.get("voltar")
    redirect(home)