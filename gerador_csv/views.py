from django.shortcuts import render, redirect
from django.http import HttpResponse
import csv

def index(request):
    return render(request, 'index.html')

def gerador_view(request):
    #funcao principal
    pass


#------------------------Validações de Formulário------------------------

def coletar_dados(request):
    if request.method == 'POST':
        nlinhas = int(request.POST['nlinhas'])
        tipo_dado = request.POST['tipoDado']

        categorias = ["Nome","CPF","Idade","Cidade","Profissão"]

        print(nlinhas)
        print(categorias)
        print(tipo_dado)


        #Utilizando classe de validação
        if ValidaFormulario.valida_nlinhas(nlinhas) is True:
            print('As linhas foram validadas com sucesso.')
        else:
            print('Linhas invalidas.')

        gera_csv(nlinhas, categorias)


        resposta = f"Os dados enviados foram: {request.POST['nlinhas']} e {request.POST['tipoDado']}"
        return HttpResponse(resposta)
    
    return render(request, 'index.html')

#------------------------Lógica para Gerar Csv------------------------

def preenchimento_dados(nlinhas, categorias):

    dados_csv = []
    #n_campos = len(categorias)

    dados_csv.append(categorias) #Nome dos campos, primeira linha

    for linha in range(nlinhas):
        registro = [f"Nome{linha}",f"CPF{linha}",f"Idade{linha}",f"Cidade{linha}",f"Profissão{linha}"]
        dados_csv.append(registro)
    
    return dados_csv

def gera_csv(nlinhas, categorias):

    dados_csv = preenchimento_dados(nlinhas, categorias)

    nome_arquivo = 'dados.csv'

    with open(nome_arquivo, 'w', newline='') as arquivo_csv:
        writer = csv.writer(arquivo_csv)
        writer.writerows(dados_csv)

    print(f'O arquivo {nome_arquivo} foi criado com sucesso.')
    print(dados_csv)

#------------------------Configuração de categorias------------------------



#------------------------Validações de Formulário------------------------
class ValidaFormulario:

    @staticmethod
    def valida_nlinhas(nlinhas):
        if nlinhas > 0:
            return True
        print("Insira um número maior do que 0.")
        return False

