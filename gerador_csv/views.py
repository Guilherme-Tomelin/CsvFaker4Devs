from django.shortcuts import render, redirect
from django.http import HttpResponse
import csv

def index(request):
    if request.method == 'POST':
        nome_arquivo = request.POST.get('nomeArquivo')
        n_linhas = int(request.POST.get('nlinhas'))
        campos = request.POST.getlist('nome_campo_usuario[]')
        tipos_dados = request.POST.getlist('tipoDado[]')
        campos_adicionais = request.POST.getlist('campoAdicional[]')

        print("entrou na função")
        print(nome_arquivo)
        print(n_linhas)
        print(campos)
        print(tipos_dados)
        print(campos_adicionais)

    return render(request, 'index.html')

def gerar_csv(request):
    if request.method == 'POST':
        nome_arquivo = request.POST.get('nomeArquivo')
        n_linhas = int(request.POST.get('nlinhas'))
        campos = request.POST.getlist('nome_campo_usuario[]')
        tipos_dados = request.POST.getlist('tipoDado[]')
        campos_adicionais = request.POST.getlist('campoAdicional[]')

        print("entrou na função")
        print(nome_arquivo)
        print(n_linhas)
        print(campos)
        print(tipos_dados)
        print(campos_adicionais)

    return redirect('index')

