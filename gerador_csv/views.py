from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def coletar_dados(request):
    if request.method == 'POST':
        nlinhas = request.POST['nlinhas']
        tipo_dado = request.POST['tipoDado']

        print(nlinhas)
        print(tipo_dado)


        resposta = f"Os dados enviados foram: {request.POST['nlinhas']} e {request.POST['tipoDado']}"
        return HttpResponse(resposta)
    
    return render(request, 'index.html')